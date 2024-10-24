import webbrowser
import streamlit as st
from source.voice_manager import dawia_say

def search_google(prompt):
    """search google for a query"""
    to_search = prompt.split("for")[-1]
    url = f"https://google.com/search?q={to_search}"
    webbrowser.get().open(url)
    with st.sidebar:
        st.success(f"Searching for {to_search}...")
    text = f"Searching for {to_search}..."
    dawia_say(text)

def search_youtube(prompt):
    """search youtube for a query"""
    to_search = prompt.split("for")[-1]
    url = f"https://youtube.com/search?q={to_search}"
    webbrowser.get().open(url)
    with st.sidebar:
        st.success(f"Searching for {to_search} on YouTube...")
    text = f"Searching for {to_search} on YouTube..."
    dawia_say(text)

def search_wikipedia(prompt):
    """search wikipedia for a query"""
    to_search = prompt.split("for")[-1].strip()
    url = f"https://en.wikipedia.org/wiki/{to_search}"
    webbrowser.get().open(url)
    with st.sidebar:
        st.success(f"Searching Wikipedia for {to_search}...")
    text = f"Searching Wikipedia for {to_search}..."
    dawia_say(text)
