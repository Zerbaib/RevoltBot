import json
import os

config_file_path = "config.json"

if not os.path.exists(config_file_path):
    with open(config_file_path, 'w') as config_file:
        token = input("Enter the bot's token:\n")
        prefix = input("Enter the bot's prefix:\n")
        config_data = {
            "TOKEN": token,
            "PREFIX": prefix
        }
        json.dump(config_data, config_file, indent=4)

def load_config():
    with open(config_file_path) as f:
        data = json.load(f)
        return data["TOKEN"], data["PREFIX"]
