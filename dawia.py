from mistralai import Mistral
import speech_recognition as sr
import edge_tts
import os
from playsound import playsound


voice = "en-GB-SoniaNeural"
model = "mistral-tiny"
api_key = open("api_key", "r").read()


def init_mistral(api_key):
    """Initialize the Mistral client."""
    client = Mistral(api_key=api_key)
    return client

def get_response(text, client):
    """Get the response from Mistral API."""
    response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": text}],
    )
    dawia_response = response.choices[0].message.content
    return dawia_response

def text_to_voice(text, voice):
    """Convert text to dawia voice."""
    output_file = ".tmp.mp3"
    communicate = edge_tts.Communicate(text, voice)
    with open(output_file, "wb") as file:
        for chunk in communicate.stream_sync():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
    return output_file

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
    except sr.RequestError:
        return "Sorry, I could not process your request at the moment."
    
def main():
    print("initializing Dawia...")
    init = init_mistral(api_key)
    if init:
        print("Dawia Initialized")
        print(init)
        print("transcribing audio...")
        txt = "whats the distance between earth and mars"
        print("getting response from Dawia ...")
        res = get_response(txt, init)
        print(res)
        dawia_voice = text_to_voice(res, voice)
        if dawia_voice:
            print("Dawia voice generated")
            print("playing Dawia voice...")
            playsound(".tmp.mp3")
            print("finished playing Dawia voice")
            os.remove(".tmp.mp3")
    else:
        print("Mistral AI failed to initialize")

if __name__ == "__main__":
    main()
