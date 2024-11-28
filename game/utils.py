import json
from logger import log_event, log_error

def load_json(file_path):
    """
    Load a JSON file and return its contents.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            log_event(f"Loaded JSON file: {file_path}")
            return data
    except FileNotFoundError:
        log_error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        log_error(f"JSON decode error in {file_path}: {e}")
        return {}

def clamp(value, min_value, max_value):
    """
    Clamp a value between a minimum and maximum range.
    """
    return max(min_value, min(value, max_value))

def calculate_percentage(current, maximum):
    """
    Calculate the percentage of a current value relative to a maximum value.
    """
    if maximum == 0:
        log_error("Division by zero in calculate_percentage.")
        return 0
    return (current / maximum) * 100

def is_key_in_dict(dictionary, key):
    """
    Check if a key exists in a dictionary.
    """
    return key in dictionary

def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries, with values from dict2 overwriting those in dict1.
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged

