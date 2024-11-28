from constants import CONFIG_PATH
from utils import load_json
from logger import log_event

# Global variable for storing boss data
boss_definitions = {}

def load_bosses(file_path=None):
    """
    Load boss definitions from a JSON file.
    """
    global boss_definitions
    file_path = file_path or CONFIG_PATH + "boss.json"
    boss_definitions = load_json(file_path)
    log_event("Bosses loaded successfully.")

def initialize_boss(name):
    """
    Initialize a boss by name with its zones and abilities.
    """
    boss_data = next((boss for boss in boss_definitions.get("bosses", []) if boss["name"] == name), None)
    if not boss_data:
        log_event(f"Boss {name} not found.", level="error")
        return None

    # Create a boss instance
    boss_instance = {
        "name": boss_data["name"],
        "description": boss_data["description"],
        "zones": {zone["name"]: {"health": zone["health"], "abilities": zone["abilities"]} for zone in boss_data["zones"]},
        "global_abilities": boss_data.get("global_abilities", [])
    }
    log_event(f"Boss {name} initialized.")
    return boss_instance

def update_boss(boss, player_actions):
    """
    Update the boss's state based on player actions.
    """
    for zone_name, zone_data in boss["zones"].items():
        if zone_name in player_actions.get("attacks", {}):
            damage = player_actions["attacks"][zone_name]
            zone_data["health"] -= damage
            log_event(f"{zone_name} of boss {boss['name']} took {damage} damage. Remaining health: {zone_data['health']}")

def apply_boss_ability(boss, ability_name, targets):
    """
    Apply a boss's global ability to targets.
    """
    ability = next((ab for ab in boss["global_abilities"] if ab["name"] == ability_name), None)
    if not ability:
        log_event(f"Ability {ability_name} not found for boss {boss['name']}.", level="error")
        return

    # Example effect application
    if "damage" in ability:
        for target in targets:
            target["health"] -= ability["damage"]
            log_event(f"{ability_name} dealt {ability['damage']} damage to target.")

def render_boss(boss):
    """
    Render the boss's zones and their statuses.
    """
    for zone_name, zone_data in boss["zones"].items():
        log_event(f"Zone {zone_name}: Health {zone_data['health']}")

def is_boss_defeated(boss):
    """
    Check if all boss zones are defeated.
    """
    return all(zone["health"] <= 0 for zone in boss["zones"].values())

