"""This module contains functions to interact with the Mistral API."""


from time import sleep
from mistralai import Mistral
import streamlit as st


def init_mistral(api_key):
    """Initialize the Mistral client."""
    return Mistral(api_key=api_key)

def get_response(client, messages):
    """Get the response from Mistral API."""
    response = client.chat.complete(
        model=st.session_state["mistral_model"],
        messages=messages
    )
    return response.choices[0].message.content

def get_response_check(client, msg):
    """Get the response from Mistral API."""
    response = client.chat.complete(
        model="mistral-tiny",
        messages=[{"role": "user", "content": msg}],
    )
    dawia_response = response.choices[0].message.content
    return dawia_response


def stream_response(full_response):
    """Stream the full response in chunks."""
    for chunk in full_response:
        yield chunk
        sleep(0.03)
