import json
import os

CONFIG_FILE = "config.json"

def load_config():
    """Load the config from the JSON file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        #Def cfg
        return {"model": "mistral-tiny", "convert_to_audio": False, "voice_dawia": "en-GB-SoniaNeural", "user_logo": "./assets/user_img/user_01.png"}

def save_config(config):
    """Save the config to the JSON file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f , indent=4)
