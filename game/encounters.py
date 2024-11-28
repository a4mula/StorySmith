import random
from logger import log_event
from storyteller import advance_story
from boss import initialize_boss, update_boss
from classes import apply_ability_effect

# Global variable for active encounters
active_encounter = None

def generate_random_encounter(encounter_pool):
    """
    Generate a random encounter from the provided encounter pool.
    """
    encounter = random.choice(encounter_pool)
    log_event(f"Random encounter generated: {encounter['name']}")
    return encounter

def trigger_scripted_encounter(encounter_data):
    """
    Trigger a specific scripted encounter.
    """
    global active_encounter
    active_encounter = encounter_data
    log_event(f"Scripted encounter triggered: {active_encounter['name']}")

def resolve_encounter(player_action):
    """
    Resolve the active encounter based on the player's action.
    """
    global active_encounter
    if not active_encounter:
        log_event("No active encounter to resolve.", level="error")
        return

    if player_action in active_encounter["outcomes"]:
        outcome = active_encounter["outcomes"][player_action]
        apply_encounter_effect(outcome)
        log_event(f"Encounter resolved with action: {player_action}")
        active_encounter = None
    else:
        log_event(f"Invalid action: {player_action} for encounter {active_encounter['name']}", level="error")

def apply_encounter_effect(outcome):
    """
    Apply the effects of an encounter outcome.
    """
    if "health_change" in outcome:
        log_event(f"Player health changed by {outcome['health_change']}.")
        # Update health in the game state (implementation required)
    if "next_scene" in outcome:
        advance_story(outcome["next_scene"])
    if "boss_trigger" in outcome:
        initialize_boss(outcome["boss_trigger"])

def update_encounters(game_state):
    """
    Update encounter logic dynamically based on the game state.
    """
    # Example: Trigger an encounter if certain conditions are met
    if "encounter_trigger" in game_state:
        trigger_scripted_encounter(game_state["encounter_trigger"])

