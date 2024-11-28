import unittest
import json
import jsonschema
from jsonschema import validate

class TestJsonSchemas(unittest.TestCase):
    """Test the structure and integrity of JSON configuration files."""

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for JSON schema validation."""
        cls.schemas = {
            "settings": {
                "type": "object",
                "properties": {
                    "resolution": {"type": "object", "properties": {"width": {"type": "integer"}, "height": {"type": "integer"}}, "required": ["width", "height"]},
                    "audio": {"type": "object", "properties": {"volume": {"type": "integer"}, "mute": {"type": "boolean"}}, "required": ["volume", "mute"]},
                    "gameplay": {"type": "object", "properties": {"difficulty": {"type": "string"}, "autosave": {"type": "boolean"}}, "required": ["difficulty", "autosave"]},
                    "controls": {"type": "object"},
                    "graphics": {"type": "object"},
                    "debug": {"type": "object"},
                },
                "required": ["resolution", "audio", "gameplay"]
            },
            "classes": {
                "type": "object",
                "properties": {
                    "classes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "description": {"type": "string"},
                                "attributes": {"type": "object"},
                                "abilities": {"type": "array"}
                            },
                            "required": ["name", "description", "attributes", "abilities"]
                        }
                    }
                },
                "required": ["classes"]
            },
            "story": {
                "type": "object",
                "properties": {
                    "start_scene": {"type": "string"},
                    "scenes": {
                        "type": "object",
                        "additionalProperties": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"},
                                "choices": {"type": "array"}
                            },
                            "required": ["text", "choices"]
                        }
                    }
                },
                "required": ["start_scene", "scenes"]
            },
            "boss": {
                "type": "object",
                "properties": {
                    "bosses": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "zones": {"type": "array"},
                                "global_abilities": {"type": "array"}
                            },
                            "required": ["name", "zones", "global_abilities"]
                        }
                    }
                },
                "required": ["bosses"]
            }
        }
        cls.test_files = {
            "settings": "config/settings.json",
            "classes": "config/classes.json",
            "story": "config/story.json",
            "boss": "config/boss.json"
        }

    def test_json_schemas(self):
        """Validate JSON files against their respective schemas."""
        for key, file_path in self.test_files.items():
            with self.subTest(file=file_path):
                try:
                    # Load the JSON file
                    with open(file_path, "r") as file:
                        data = json.load(file)

                    # Validate against the schema
                    schema = self.schemas[key]
                    validate(instance=data, schema=schema)
                except jsonschema.exceptions.ValidationError as e:
                    self.fail(f"{file_path} failed schema validation: {e.message}")
                except FileNotFoundError:
                    self.fail(f"{file_path} does not exist.")
                except json.JSONDecodeError as e:
                    self.fail(f"{file_path} contains invalid JSON: {e.msg}")

if __name__ == "__main__":
    unittest.main()

