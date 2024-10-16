import streamlit as st
from concurrent.futures import ThreadPoolExecutor
from streamlit_image_select import image_select
from source.config_manager import load_config, save_config
from source.response_manager import init_mistral, get_response, stream_response
from source.voice_manager import text_to_voice, listen_and_transcribe
from source.local_db_manager import load_chat_history, save_chat_history
from source.tools_manager import term_in_prompt, img_to_base64, program_launcher
from streamlit_google_auth import Authenticate
from hvar import page_title

st.set_page_config(page_icon="./assets/img/favicon.ico")
dawia_logo = img_to_base64("./assets/img/dawia.png")

st.markdown(page_title, unsafe_allow_html=True)
st.title("Your personal voice assistant.")

authenticator = Authenticate(
    secret_credentials_path='google_credentials.json',
    cookie_name='dawiassit',
    cookie_key='secret_cookie_key',
    redirect_uri='http://localhost:8501',
)
authenticator.check_authentification()

if st.session_state.get('connected'):


#----------------- Constants
    DAWIA_AVATAR = "./assets/img/favicon.ico"
    restriction2 = "? answer in one short sentence"
    #api_key = open("api_key", "r").read()

    config = load_config()

    # --------default values from config
    if "mistral_model" not in st.session_state:
        st.session_state["mistral_model"] = config["model"]

    if "voice_dawia" not in st.session_state:
        st.session_state["voice_dawia"] = config["voice_dawia"]

    if "convert_to_audio" not in st.session_state:
        st.session_state["convert_to_audio"] = config["convert_to_audio"]

    if "user_logo" not in st.session_state:
        st.session_state["user_logo"] = config["user_logo"]
    #-----------------------------------------------#

    # sidebar---------------------------#
    with st.sidebar:
        if st.button('Log out'):
            authenticator.logout()
        st.title("Configure your :red[API key]")
        api_key = st.text_input("Please paste your Mistral API key here:", placeholder="API_KEY", type="password")

        if st.button("Clear chat log"):
            st.session_state.messages = []
            save_chat_history([])
            prompt = None
            audio = None


        convert_to_audio = st.toggle("Toggle voice response", value=st.session_state["convert_to_audio"])
        selected_model = st.selectbox(
            "Select a model",
            ("pixtral-12b", "mistral-small", "mistral-tiny"),
            index=["pixtral-12b", "mistral-small", "mistral-tiny"].index(st.session_state["mistral_model"])
        )

        selected_voice = st.selectbox(
            "Select Dawia's voice",
            ("en-GB-SoniaNeural", "en-US-AriaNeural", "en-US-JennyNeural", "en-US-MichelleNeural"),
            index=["en-GB-SoniaNeural", "en-US-AriaNeural", "en-US-JennyNeural", "en-US-MichelleNeural"].index(st.session_state["voice_dawia"])
        )

        st.write("Select your avatar")
        logo_container = st.container(height=300, border=False)
        with logo_container:
            user_logo = image_select(
                use_container_width=False,
                label="",
                images=["./assets/user_img/user_01.png",
                        "./assets/user_img/user_02.png",
                        "./assets/user_img/user_03.png",
                        "./assets/user_img/user_04.png",
                        "./assets/user_img/user_05.png",
                        "./assets/user_img/user_06.png",
                        "./assets/user_img/user_07.png",
                        "./assets/user_img/user_08.png"],
                index=["./assets/user_img/user_01.png",
                    "./assets/user_img/user_02.png",
                    "./assets/user_img/user_03.png",
                    "./assets/user_img/user_04.png",
                    "./assets/user_img/user_05.png",
                    "./assets/user_img/user_06.png",
                    "./assets/user_img/user_07.png",
                    "./assets/user_img/user_08.png"].index(st.session_state["user_logo"])
            )

        if convert_to_audio != st.session_state["convert_to_audio"]:
            st.session_state["convert_to_audio"] = convert_to_audio
            config["convert_to_audio"] = convert_to_audio
            save_config(config)
            st.rerun()

        if selected_model != st.session_state["mistral_model"]:
            st.session_state["mistral_model"] = selected_model
            config["model"] = selected_model
            save_config(config)
            st.rerun()

        if selected_voice != st.session_state["voice_dawia"]:
            st.session_state["voice_dawia"] = selected_voice
            config["voice_dawia"] = selected_voice
            save_config(config)
            st.rerun()

        if user_logo != st.session_state["user_logo"]:
            st.session_state["user_logo"] = user_logo
            config["user_logo"] = user_logo
            save_config(config)
            st.rerun()

    #-------------main page---------------#
    client = init_mistral(api_key)
    if "messages" not in st.session_state:
        st.session_state.messages = load_chat_history()

    chat_container = st.container(height=700, border=False)

    left, right = st.columns([10, 1], vertical_alignment="bottom")
    chat = left.chat_input("Message Dawia")
    voice_btn = right.button("🔊")
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                avatar = st.session_state["user_logo"]
            else:
                avatar = DAWIA_AVATAR
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])

    if voice_btn:
        prompt = listen_and_transcribe()
    else:
        prompt = chat

    print("prompt", prompt)
    if prompt:
        with chat_container:
            if term_in_prompt(["open", "launch", "start", "execute"], prompt):
                test = program_launcher(prompt)
                st.stop()
            else:
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user", avatar=st.session_state["user_logo"]):
                    st.markdown(prompt)

                with st.chat_message("system", avatar=DAWIA_AVATAR):
                    message_placeholder = st.empty()

                    messages_for_mistral = st.session_state.messages + [{"role": "user", "content": prompt + restriction2}] + [{"role": "system", "content": "If asked about your name your name is Dawia never say mistral as your name, you're a personal assistant."}]

                    full_response = get_response(client, messages_for_mistral)
                    with ThreadPoolExecutor() as executor:
                        if st.session_state["convert_to_audio"]:
                            executor.submit(text_to_voice, full_response, st.session_state["voice_dawia"])
                            message_placeholder.write_stream(stream_response(full_response))
                            executor.shutdown()

                        else:
                            message_placeholder.write_stream(stream_response(full_response))

        st.session_state.messages.append({"role": "system", "content": full_response})

    save_chat_history(st.session_state.messages)
else:
    st.write('Please login with your google account to continue')
    authorization_url = authenticator.get_authorization_url()
    st.link_button('Login', authorization_url)
