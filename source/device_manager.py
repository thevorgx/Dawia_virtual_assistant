from yeelight import Bulb

CLIENT_FILE = "./source/device_client"
CLIENT = open(CLIENT_FILE, "r").read()

device = Bulb(CLIENT)

def turn_on_light():
    """Turn on the light."""
    device.turn_on()

def turn_off_light():
    """Turn off the light."""
    device.turn_off()

def toggle_light():
    """Toggle the light."""
    device.toggle()
