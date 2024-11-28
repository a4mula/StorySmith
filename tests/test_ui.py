import unittest
from game.ui import initialize_ui, render_ui, handle_ui_events, update_ui

class TestUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for UI tests."""
        cls.default_ui_state = {
            "scene_text": "",
            "choices": [],
            "health_bar": 100,
            "mana_bar": 100
        }
        cls.mock_game_state = {
            "current_scene": {
                "text": "You find yourself in a dark forest.",
                "choices": [{"option": "Enter the forest", "next_scene": "forest_path"}]
            },
            "player_stats": {"health": 80, "mana": 50}
        }

    def setUp(self):
        """Reset UI state before each test."""
        self.ui_state = initialize_ui()

    # UI Initialization Tests
    def test_initialize_ui(self):
        """Test that the UI initializes with default values."""
        self.assertEqual(self.ui_state["scene_text"], "", "Scene text should initialize as empty.")
        self.assertEqual(self.ui_state["choices"], [], "Choices should initialize as an empty list.")
        self.assertEqual(self.ui_state["health_bar"], 100, "Health bar should initialize to 100.")
        self.assertEqual(self.ui_state["mana_bar"], 100, "Mana bar should initialize to 100.")

    # Rendering Tests
    def test_render_ui(self):
        """Test rendering static UI components."""
        try:
            render_ui(self.ui_state)
        except Exception as e:
            self.fail(f"Rendering UI raised an exception: {e}")

    def test_render_dynamic_ui(self):
        """Test rendering dynamic UI elements based on game state."""
        self.ui_state["scene_text"] = self.mock_game_state["current_scene"]["text"]
        self.ui_state["choices"] = self.mock_game_state["current_scene"]["choices"]
        self.ui_state["health_bar"] = self.mock_game_state["player_stats"]["health"]
        self.ui_state["mana_bar"] = self.mock_game_state["player_stats"]["mana"]

        try:
            render_ui(self.ui_state)
        except Exception as e:
            self.fail(f"Dynamic UI rendering raised an exception: {e}")

    # Event Handling Tests
    def test_handle_ui_events(self):
        """Test handling player input through the UI."""
        mock_event = {"type": "choice", "selection": 0}
        handle_ui_events(self.ui_state, mock_event)
        self.assertEqual(self.ui_state["selected_choice"], 0, "UI did not handle the input event correctly.")

    # Integration Tests
    def test_update_ui(self):
        """Test that UI updates reflect changes in game state."""
        update_ui(self.ui_state, self.mock_game_state)
        self.assertEqual(self.ui_state["scene_text"], "You find yourself in a dark forest.",
                         "UI did not update scene text correctly.")
        self.assertEqual(self.ui_state["choices"], [{"option": "Enter the forest", "next_scene": "forest_path"}],
                         "UI did not update choices correctly.")
        self.assertEqual(self.ui_state["health_bar"], 80, "UI did not update health bar correctly.")
        self.assertEqual(self.ui_state["mana_bar"], 50, "UI did not update mana bar correctly.")

if __name__ == "__main__":
    unittest.main()

