import unittest
import time
from game.stage_manager import render_stage
from game.ui import render_ui, update_ui
from game.encounters import generate_random_encounter
from game.constants import load_settings

class TestPerformance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for performance tests."""
        cls.mock_stage = {
            "layers": {"background": [], "midground": [], "foreground": []},
            "props": [{"name": "tree", "position": (100, 200), "layer": "background"}],
            "animations": []
        }
        cls.mock_ui_state = {
            "scene_text": "You find yourself in a dark forest.",
            "choices": [{"option": "Enter the forest", "next_scene": "forest_path"}],
            "health_bar": 100,
            "mana_bar": 50
        }
        cls.mock_game_state = {
            "player_stats": {"health": 100, "mana": 50},
            "scene": "forest"
        }

    # Rendering Performance Tests
    def test_render_stage_performance(self):
        """Benchmark rendering performance for stages."""
        start_time = time.time()
        render_stage(self.mock_stage)
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 0.05, f"Stage rendering took too long: {duration:.3f} seconds")

    def test_render_ui_performance(self):
        """Benchmark rendering performance for the UI."""
        start_time = time.time()
        render_ui(self.mock_ui_state)
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 0.05, f"UI rendering took too long: {duration:.3f} seconds")

    # Encounter Generation Performance Test
    def test_generate_random_encounter_performance(self):
        """Benchmark encounter generation performance."""
        start_time = time.time()
        for _ in range(1000):  # Generate a large number of encounters
            generate_random_encounter()
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 1.0, f"Random encounter generation took too long: {duration:.3f} seconds")

    # Data Update Performance Test
    def test_update_ui_performance(self):
        """Benchmark performance for updating UI with game state."""
        start_time = time.time()
        update_ui(self.mock_ui_state, self.mock_game_state)
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 0.05, f"UI update took too long: {duration:.3f} seconds")

    def test_load_settings_performance(self):
        """Benchmark performance of loading settings."""
        start_time = time.time()
        settings = load_settings("config/settings.json")
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 0.02, f"Settings loading took too long: {duration:.3f} seconds")

if __name__ == "__main__":
    unittest.main()

