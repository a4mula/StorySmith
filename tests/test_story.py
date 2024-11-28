import unittest
from game.storyteller import load_story, get_start_scene, get_scene_choices, transition_to_scene

class TestStory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for story tests."""
        # Load valid and partial test data
        cls.valid_story = load_story("test_data/valid/valid_story.json")
        cls.partial_story = load_story("test_data/partial/partial_story.json")

    def setUp(self):
        """Reset the story state for each test."""
        self.current_scene = get_start_scene(self.valid_story)

    # Data Validation Tests
    def test_load_story_valid(self):
        """Test loading valid story data."""
        self.assertIsInstance(self.valid_story, dict, "Story data should be a dictionary.")
        self.assertIn("scenes", self.valid_story, "Valid story data should include 'scenes'.")

    def test_load_story_invalid_file(self):
        """Test behavior when story.json is missing."""
        with self.assertRaises(FileNotFoundError):
            load_story("test_data/invalid/nonexistent_story.json")

    # Narrative Handling Tests
    def test_start_scene(self):
        """Test loading the start scene."""
        start_scene = get_start_scene(self.valid_story)
        self.assertEqual(start_scene["text"], "You find yourself at the edge of a dark forest. What will you do?")
        self.assertIn("choices", start_scene, "Start scene should contain choices.")

    def test_scene_transition(self):
        """Test transitioning between scenes."""
        next_scene = transition_to_scene(self.valid_story, "forest_path")
        self.assertEqual(next_scene["text"], "The forest is dark and full of strange noises. A shadow moves ahead.")
        self.assertIn("choices", next_scene, "Next scene should contain choices.")

    # Event Trigger Tests
    def test_event_activation(self):
        """Test triggering events based on player choices."""
        scene_choices = get_scene_choices(self.valid_story, "intro")
        choice = scene_choices[0]  # Example: "Enter the forest"
        self.assertEqual(choice["next_scene"], "forest_path", "Event did not trigger the correct next scene.")

    # Integration Tests
    def test_story_to_ui_updates(self):
        """Test that UI reflects story progression."""
        scene = self.current_scene
        # Mock UI update logic
        self.assertIn("text", scene, "UI should reflect story text.")
        self.assertIn("choices", scene, "UI should display story choices.")

    def test_story_to_class_integration(self):
        """Test that class traits influence narrative branching."""
        # Mock class trait affecting narrative
        class_traits = {"strength": 20}  # Example: Warrior with high strength
        next_scene = transition_to_scene(self.valid_story, "forest_path", class_traits)
        self.assertEqual(next_scene["text"], "The forest opens to reveal a hidden path. Your strength helped clear the way.")

if __name__ == "__main__":
    unittest.main()

