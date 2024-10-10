from mistralai import Mistral
import speech_recognition as sr
import edge_tts
import os

"""Backend for Dawia"""


voice = "en-GB-SoniaNeural"
model = "mistral-tiny"

def init_mistral(api_key):
    client = Mistral(api_key=api_key)
    return client

def get_response(text, client):
    response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content

def text_to_voice(text):
    output_file = ".tmp.mp3"
    communicate = edge_tts.Communicate(text, voice)
    with open(output_file, "wb") as file:
        for chunk in communicate.stream_sync():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
    return output_file

def transcribe_audio(audio_file_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as srs:
        audio_data = r.record(srs)
    try:
        return r.recognize_google(audio_data)
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."
    except sr.RequestError:
        return "Sorry, I could not process your request at the moment."
