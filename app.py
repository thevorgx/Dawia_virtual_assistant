import streamlit as st
from audio_recorder_streamlit import audio_recorder
from source.dawia import (
    init_mistral,
    transcribe_audio,
    img_to_base64,
    get_response,
    load_chat_history,
    save_chat_history,
    stream_response,
    USER_AVATAR,
    DAWIA_AVATAR
)

with open("./source/api_key", "r") as file:
    api_key = file.read().strip()

ghub_logo = img_to_base64("./assets/img/git.png")
dawia_logo = img_to_base64("./assets/img/dawia.png")


st.title("Dawia, Your personal voice assistant.")

client = init_mistral(api_key)

if "mistral_model" not in st.session_state:
    st.session_state["mistral_model"] = "mistral-tiny"

if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])

chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        avatar = USER_AVATAR if message["role"] == "user" else DAWIA_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

speech_data = audio_recorder(text="", icon_size="1x", icon_name="bolt", neutral_color="#557C56", recording_color="#ff4b4b")

if prompt := st.chat_input("How can I help?"):
    with chat_container:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar=DAWIA_AVATAR):
            message_placeholder = st.empty()

            messages_for_mistral = st.session_state.messages + [
                {"role": "user", "content": prompt},
                {"role": "system", "content": "You are Dawia, a helpful and friendly virtual assistant. Always provide clear, concise, and polite responses."}
            ]

            full_response = get_response(client, messages_for_mistral)
            message_placeholder.write_stream(stream_response(full_response))

    st.session_state.messages.append({"role": "assistant", "content": full_response})

save_chat_history(st.session_state.messages)
