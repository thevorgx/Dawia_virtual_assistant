import streamlit as st
import shelve
import base64
import speech_recognition as sr
from mistralai import Mistral
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

def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages
