import streamlit as st
import os
from source.dawia import init_mistral, get_response, text_to_voice
from playsound import playsound
"""frontend for Dawia"""


with open("./source/api_key", "r") as file:
    api_key = file.read().strip()

st.title("Dawia Voice Assistant")

user_input = st.text_area("Ask Dawia:", "What's the distance between Earth and Mars?")

if st.button("Get Response"):
    with st.spinner("Initializing Dawia..."):
        client = init_mistral(api_key)

    if client:
        with st.spinner("Getting response..."):
            response_text = get_response(user_input, client)
        
        with st.spinner("Converting response to voice..."):
            audio_file = text_to_voice(response_text)
        
        if audio_file:
            playsound(audio_file)
            st.success("Dawia's Response: " + response_text)
            os.remove(audio_file)
        else:
            st.error("Failed to generate voice")
    else:
        st.error("Failed to initialize LLM.")
