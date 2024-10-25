"""This module contains tools for the main program."""

import base64
import subprocess
import streamlit as st
from source.voice_manager import dawia_say


def program_launcher(prompt):
    """Launch a program from the prompt."""
    program_name = prompt.split()[-1]
    subprocess.Popen(['start', program_name], shell=True)
    with st.sidebar:
        st.success(f"Opening {program_name}...")
    text = f"Opening {program_name}"
    dawia_say(text)


def img_to_base64(file_path):
    """Convert an image to base64 string to display it using HTML."""
    with open(file_path, "rb") as img:
        b64_string = base64.b64encode(img.read()).decode("utf-8")
    return b64_string

def term_in_prompt(terms, prompt):
    """Check if any of the terms list is in the prompt."""
    prompt = prompt.lower()
    for term in terms:
        if term.lower() in prompt:
            return True
