import streamlit as st
import os
import pickle
import base64
import speech_recognition as sr
from mistralai import Mistral
from time import sleep
"""Dawia's backend functions."""

USER_AVATAR = "👤"
DAWIA_AVATAR = "💭"

def init_mistral(api_key):
    """Initialize the Mistral client."""
    return Mistral(api_key=api_key)

def transcribe_audio(audio_file_path):
    """Transcribe the audio file to text."""
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as srs:
        audio_data = r.record(srs)
    try:
        txt = r.recognize_google(audio_data)
        return txt
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."
    except sr.RequestError as e:
        return "Sorry, I could not process your request at the moment."

def img_to_base64(file_path):
    """Convert an image to base64 string to display it using HTML."""
    with open(file_path, "rb") as img:
        b64_string = base64.b64encode(img.read()).decode("utf-8")
    return b64_string

def get_response(client, messages):
    """Get the response from Mistral API."""
    response = client.chat.complete(
        model=st.session_state["mistral_model"],
        messages=messages
    )
    return response.choices[0].message.content

def what_prompt(chat, audio):
    if chat:
        return chat
    
    elif audio:
        req_audio_file = ".tmp_query_req.mp3"
        with open(req_audio_file, "wb") as file:
            file.write(audio)
        return transcribe_audio(req_audio_file)
    return None

def load_chat_history():
    if os.path.exists("chat_history.pkl"):
        with open("chat_history.pkl", 'rb') as f:
            return pickle.load(f)
    else:
        return []

def save_chat_history(messages):
    with open('chat_history.pkl', 'wb') as f:
        pickle.dump(messages, f)

def stream_response(full_response):
    """Stream the full response in chunks."""
    for chunk in full_response:
        yield chunk
        sleep(0.1)
