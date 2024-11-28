import json
from constants import CONFIG_PATH

class ClassManager:
    def __init__(self, file_path=None):
        """Initialize the Class Manager."""
        self.file_path = file_path or CONFIG_PATH + "classes.json"
        self.classes = self.load_classes(self.file_path)

    def load_classes(self, file_path):
        """Load and validate class definitions from a JSON file."""
        try:
            with open(file_path, "r") as file:
                classes = json.load(file)
            self.validate_classes(classes)
            return classes["classes"]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading classes: {e}")
            return []

    def validate_classes(self, classes):
        """Ensure all class definitions have required fields."""
        required_keys = ["name", "attributes", "abilities"]
        for cls in classes["classes"]:
            if not all(key in cls for key in required_keys):
                raise ValueError(f"Class {cls.get('name', 'Unknown')} is missing required keys.")

    def get_class_by_name(self, name):
        """Retrieve a class definition by its name."""
        return next((cls for cls in self.classes if cls["name"] == name), None)

    def modify_class_stat(self, class_name, stat, value):
        """Modify a specific stat for a given class."""
        cls = self.get_class_by_name(class_name)
        if cls and stat in cls["attributes"]:
            cls["attributes"][stat] += value
            print(f"{class_name}'s {stat} modified by {value}. New value: {cls['attributes'][stat]}")
        else:
            print(f"Invalid class or stat: {class_name}, {stat}")

    def execute_ability(self, class_name, ability_name, target):
        """Execute a class ability and apply its effects."""
        cls = self.get_class_by_name(class_name)
        if cls:
            ability = next((ab for ab in cls["abilities"] if ab["name"] == ability_name), None)
            if ability:
                print(f"Executing {ability_name} from {class_name} on {target['name']}")
                # Example effect application (expand as needed)
                if ability["effect"] == "damage":
                    target["health"] -= ability["damage"]
                elif ability["effect"] == "stun":
                    target["status"] = "stunned"
            else:
                print(f"Ability {ability_name} not found for class {class_name}.")
        else:
            print(f"Class {class_name} not found.")

