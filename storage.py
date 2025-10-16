
# JSON load/save helpers

import json
import os
from typing import Any

def load_json(filepath: str) -> list:
    """ Loads data from a JSON file. Returns an empty list if the file doesn't exist."""

    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding = "utf-8") as f:
        try :
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def save_json(filepath: str, data: list):
    """ Saves data to a JSON file. """
    
    os.makedirs(os.path.dirname(filepath), exist_ok = True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)