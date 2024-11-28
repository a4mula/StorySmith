import unittest
from game.utils import load_json
from game.classes import load_classes
from game.storyteller import load_story, transition_to_scene
from game.boss import load_bosses, initialize_boss
from game.ui import initialize_ui, update_ui

class TestDataConsistency(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for consistency tests."""
        cls.mock_game_state = {"player_stats": {"health": 100, "mana": 50}, "current_scene": None, "encounters": []}
        cls.mock_ui_state = {"health_bar": 100, "mana_bar": 50, "scene_text": ""}
        cls.mock_stage_state = {"layers": {"background": [], "midground": [], "foreground": []}}

        # Load valid data from test_data/
        cls.valid_classes = load_classes("test_data/valid/valid_classes.json")
        cls.valid_story = load_story("test_data/valid/valid_story.json")
        cls.valid_boss = load_bosses("test_data/valid/valid_boss.json")

    # JSON File Validation
    def test_json_schema_validation(self):
        """Test that JSON files adhere to expected schemas."""
        schema_files = {
            "classes": "schemas/classes_schema.json",
            "story": "schemas/story_schema.json",
            "boss": "schemas/boss_schema.json"
        }
        for file_name, schema_path in schema_files.items():
            with self.subTest(file=file_name):
                data = load_json(f"test_data/valid/valid_{file_name}.json")
                self.assertTrue(validate_json_schema(data, schema_path), f"{file_name}.json failed schema validation.")

    # Cross-Module Consistency
    def test_class_to_story_consistency(self):
        """Test that class traits align with story outcomes."""
        warrior = self.valid_classes[0]  # Example: Warrior
        scene = transition_to_scene(self.valid_story, "forest_path", traits=warrior["attributes"])
        self.assertIn("choices", scene, "Class traits did not align with story outcomes.")

    def test_story_to_boss_consistency(self):
        """Test that story outcomes trigger the correct boss encounters."""
        scene = transition_to_scene(self.valid_story, "shadow_encounter")
        boss = initialize_boss(self.valid_boss, scene["boss_encounter"])
        self.assertEqual(boss["name"], "Forest Guardian", "Incorrect boss triggered by story outcome.")

    def test_boss_to_ui_consistency(self):
        """Test that boss updates are reflected in the UI."""
        boss = initialize_boss(self.valid_boss, "Forest Guardian")
        boss["zones"][0]["health"] -= 20  # Mock damage
        update_ui(self.mock_ui_state, boss)
        self.assertEqual(self.mock_ui_state["health_bar"], 80, "UI did not reflect boss health correctly.")

    # Dynamic State Validation
    def test_runtime_updates(self):
        """Test that runtime state changes propagate correctly."""
        self.mock_game_state["player_stats"]["health"] -= 10
        update_ui(self.mock_ui_state, self.mock_game_state)
        self.assertEqual(self.mock_ui_state["health_bar"], 90, "Runtime updates did not propagate correctly.")

    # Error Handling and Edge Cases
    def test_invalid_json_handling(self):
        """Test system behavior with invalid JSON files."""
        with self.assertRaises(ValueError):
            load_classes("test_data/invalid/invalid_classes.json")

    def test_partial_json_handling(self):
        """Test system behavior with partial JSON data."""
        partial_story = load_story("test_data/partial/partial_story.json")
        scene = transition_to_scene(partial_story, "intro")
        self.assertIsNotNone(scene, "System failed to handle partial data.")

if __name__ == "__main__":
    unittest.main()

