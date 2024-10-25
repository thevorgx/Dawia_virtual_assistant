"""This module contains the functions to manage the device."""


from yeelight import Bulb
from source.tools_manager import term_in_prompt
import streamlit as st
from source.voice_manager import dawia_say

CLIENT_FILE = "./source/device_client"
CLIENT = open(CLIENT_FILE, "r").read()
device = Bulb(CLIENT)


def on_off_light(prompt):
    """Turn on or off the light"""
    prompt_on = term_in_prompt(["on"], prompt)
    prompt_off = term_in_prompt(["off"], prompt)
    device_state = device.get_properties()["power"]

    if device_state == "off" and prompt_on:
        device.turn_on()
        with st.sidebar:
            st.success("Turning on the light...")
        text = "Turning on the light..."
        dawia_say(text)

    if device_state == "off" and prompt_off:
        with st.sidebar:
            st.warning("The light is already off.")
        text = "The light is already off."
        dawia_say(text)
    
    if device_state == "on" and prompt_off:
        device.turn_off()
        with st.sidebar:
            st.success("Turning off the light...")
        text = "Turning off the light..."
        dawia_say(text)

    if device_state == "on" and prompt_on:
        with st.sidebar:
            st.warning("The light is already on.")
        text = "The light is already on."
        dawia_say(text)
