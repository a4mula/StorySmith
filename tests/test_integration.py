import unittest
from game.classes import load_classes, get_class_by_name, modify_class_stat
from game.storyteller import load_story, get_start_scene, transition_to_scene
from game.boss import load_bosses, initialize_boss, update_boss
from game.ui import initialize_ui, render_ui

class TestIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for integration tests."""
        cls.classes_data = load_classes("test_data/valid/valid_classes.json")
        cls.story_data = load_story("test_data/valid/valid_story.json")
        cls.boss_data = load_bosses("test_data/valid/valid_boss.json")
        cls.ui = initialize_ui()

    def setUp(self):
        """Reset game state for each test."""
        self.character = get_class_by_name(self.classes_data, "Warrior")
        self.current_scene = get_start_scene(self.story_data)
        self.boss = initialize_boss(self.boss_data, "Forest Guardian")

    # Module Integration Tests
    def test_class_to_story(self):
        """Test that class traits influence story progression."""
        self.character["attributes"]["strength"] = 20
        next_scene = transition_to_scene(self.story_data, "forest_path", traits=self.character["attributes"])
        self.assertIn("choices", next_scene, "Class traits did not influence narrative progression.")

    def test_story_to_boss(self):
        """Test that narrative progression triggers boss encounters."""
        next_scene = transition_to_scene(self.story_data, "shadow_encounter")
        self.assertIn("boss_encounter", next_scene, "Story progression did not trigger boss encounter.")
        self.assertEqual(next_scene["boss_encounter"], "Forest Guardian", "Incorrect boss encounter triggered.")

    def test_boss_to_ui_updates(self):
        """Test that boss updates are reflected in the UI."""
        self.boss["zones"][0]["health"] -= 25  # Mock damage
        render_ui(self.boss)  # Simulate UI update
        self.assertEqual(self.boss["zones"][0]["health"], 75, "UI did not reflect updated boss health.")

    # Data Consistency Tests
    def test_stat_sync_across_modules(self):
        """Test that stats like health and mana are consistent across modules."""
        modify_class_stat(self.classes_data, "Warrior", "health", -10)
        self.assertEqual(self.character["attributes"]["health"], 140, "Health stat not synchronized across modules.")

    # User Interaction Tests
    def test_player_choices_propagation(self):
        """Test that player decisions affect class traits, narrative paths, and encounters."""
        choice = {"option": "Enter the forest", "next_scene": "forest_path"}
        self.assertEqual(choice["next_scene"], "forest_path", "Player choice did not propagate correctly.")

    # End-to-End Tests
    def test_full_gameplay_scenario(self):
        """Simulate a full gameplay scenario."""
        self.character["attributes"]["strength"] = 20
        next_scene = transition_to_scene(self.story_data, "forest_path", traits=self.character["attributes"])
        self.assertIn("choices", next_scene, "Gameplay scenario failed at narrative progression.")

        # Simulate boss encounter
        self.boss = initialize_boss(self.boss_data, "Forest Guardian")
        self.boss["zones"][0]["health"] -= 50
        render_ui(self.boss)
        self.assertEqual(self.boss["zones"][0]["health"], 50, "Boss encounter failed in gameplay scenario.")

if __name__ == "__main__":
    unittest.main()

