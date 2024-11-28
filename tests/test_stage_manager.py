import unittest
from game.stage_manager import initialize_stage, render_stage, add_prop, remove_prop, update_stage

class TestStageManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for stage tests."""
        cls.default_stage_state = {
            "layers": {"background": [], "midground": [], "foreground": []},
            "props": [],
            "animations": []
        }
        cls.mock_game_state = {
            "scene": "forest",
            "props": [{"name": "tree", "position": (100, 200), "layer": "background"}]
        }

    def setUp(self):
        """Reset the stage state before each test."""
        self.stage_state = initialize_stage()

    # Stage Initialization Tests
    def test_initialize_stage(self):
        """Test that the stage initializes with default layers and empty state."""
        self.assertIn("layers", self.stage_state, "Stage initialization missing layers.")
        self.assertIn("props", self.stage_state, "Stage initialization missing props.")
        self.assertEqual(len(self.stage_state["layers"]["background"]), 0, "Background layer is not empty.")
        self.assertEqual(len(self.stage_state["props"]), 0, "Stage props are not empty at initialization.")

    # Rendering Tests
    def test_render_stage(self):
        """Test rendering static stage components."""
        try:
            render_stage(self.stage_state)
        except Exception as e:
            self.fail(f"Rendering stage raised an exception: {e}")

    def test_render_dynamic_stage(self):
        """Test rendering dynamic stage elements based on game state."""
        self.stage_state["props"] = self.mock_game_state["props"]
        try:
            render_stage(self.stage_state)
        except Exception as e:
            self.fail(f"Dynamic stage rendering raised an exception: {e}")

    # Prop Management Tests
    def test_add_prop(self):
        """Test adding a prop to the stage."""
        prop = {"name": "bush", "position": (50, 150), "layer": "midground"}
        add_prop(self.stage_state, prop)
        self.assertIn(prop, self.stage_state["props"], "Prop was not added to the stage correctly.")

    def test_remove_prop(self):
        """Test removing a prop from the stage."""
        prop = {"name": "tree", "position": (100, 200), "layer": "background"}
        self.stage_state["props"].append(prop)
        remove_prop(self.stage_state, prop)
        self.assertNotIn(prop, self.stage_state["props"], "Prop was not removed from the stage correctly.")

    # Integration Tests
    def test_update_stage(self):
        """Test that the stage updates dynamically based on the game state."""
        update_stage(self.stage_state, self.mock_game_state)
        self.assertEqual(self.stage_state["props"], self.mock_game_state["props"],
                         "Stage props did not update based on game state.")

if __name__ == "__main__":
    unittest.main()

