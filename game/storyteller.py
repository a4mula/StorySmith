from constants import CONFIG_PATH
from utils import load_json
from logger import log_event

# Global variables for story state
current_scene = None
story_data = {}

def load_story(file_path=None):
    """
    Load the story data from a JSON file.
    """
    global story_data, current_scene
    file_path = file_path or CONFIG_PATH + "story.json"
    story_data = load_json(file_path)
    current_scene = story_data.get("start_scene")
    log_event("Story loaded successfully.")

def get_current_scene():
    """
    Retrieve the current scene's data.
    """
    if current_scene in story_data["scenes"]:
        return story_data["scenes"][current_scene]
    log_event(f"Scene {current_scene} not found.", level="error")
    return None

def advance_story(choice_index):
    """
    Advance the story based on the player's choice.
    """
    global current_scene
    current_scene_data = get_current_scene()
    if not current_scene_data:
        return

    choices = current_scene_data.get("choices", [])
    if 0 <= choice_index < len(choices):
        next_scene = choices[choice_index]["next_scene"]
        if next_scene in story_data["scenes"]:
            log_event(f"Advancing story to scene: {next_scene}")
            current_scene = next_scene
        else:
            log_event(f"Next scene {next_scene} not found.", level="error")
    else:
        log_event(f"Invalid choice index: {choice_index}", level="error")

def get_scene_text():
    """
    Retrieve the text of the current scene.
    """
    scene_data = get_current_scene()
    return scene_data.get("text", "") if scene_data else ""

def get_scene_choices():
    """
    Retrieve the choices for the current scene.
    """
    scene_data = get_current_scene()
    return scene_data.get("choices", []) if scene_data else []

