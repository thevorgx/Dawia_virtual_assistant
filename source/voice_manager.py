"""This module contains functions for voice management(tts, stt)."""

import edge_tts
from playsound import playsound
import streamlit as st
import speech_recognition as sr
import os
import json

CONFIG_FILE = "./config.json"

def text_to_voice(text, voice):
    """Convert text to voice."""
    output_file = ".tmp_query_res.mp3"
    communicate = edge_tts.Communicate(text, voice)
    with open(output_file, "wb") as file:
        for chunk in communicate.stream_sync():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
    playsound(output_file)
    os.remove(output_file)

def listen_and_transcribe():
    """Listen to microphone input and transcribe speech to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("Listening..."):
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            #st.success(f"Transcribed Text: {text}") just for debugging
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand what you said.")
            return None
        except sr.RequestError as e:
            st.error("Sorry, I could not process your request at the moment.")
            return None


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


def dawia_say(text):
    """Convert text to voice using config settings."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
    convert_to_audio = data.get('convert_to_audio')
    if convert_to_audio:
        voice = data.get('voice_dawia') 
        text_to_voice(text, voice)
