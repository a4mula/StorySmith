import unittest
from game.encounters import generate_random_encounter, generate_scripted_encounter, process_encounter_result
from game.utils import load_json

class TestEncounters(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for encounter tests."""
        cls.valid_scripted_encounters = load_json("test_data/valid/valid_story.json")["encounters"]
        cls.partial_scripted_encounters = load_json("test_data/partial/partial_story.json").get("encounters", [])
        cls.player_state = {
            "health": 100,
            "gold": 0,
            "class": {"name": "Warrior", "attributes": {"strength": 15, "agility": 10}}
        }

    def setUp(self):
        """Reset player state for each test."""
        self.player_state["health"] = 100
        self.player_state["gold"] = 0

    # Encounter Generation Tests
    def test_generate_random_encounter(self):
        """Test generating a random encounter."""
        random_encounter = generate_random_encounter()
        self.assertIsInstance(random_encounter, dict, "Random encounter is not a dictionary.")
        self.assertIn("description", random_encounter, "Random encounter is missing a description.")
        self.assertIn("outcomes", random_encounter, "Random encounter is missing outcomes.")

    def test_generate_scripted_encounter(self):
        """Test generating a scripted encounter."""
        encounter = generate_scripted_encounter(self.valid_scripted_encounters, 1)
        self.assertIsInstance(encounter, dict, "Scripted encounter is not a dictionary.")
        self.assertEqual(encounter["id"], 1, "Scripted encounter ID does not match.")
        self.assertIn("description", encounter, "Scripted encounter is missing a description.")

    # Event Handling Tests
    def test_process_encounter_result(self):
        """Test processing an encounter result."""
        outcome = self.valid_scripted_encounters[0]["outcomes"]["fight"]
        process_encounter_result(self.player_state, outcome)
        self.assertEqual(self.player_state["gold"], 10, "Player gold did not update correctly.")
        self.assertEqual(self.player_state["health"], 90, "Player health did not decrease correctly.")

    # Integration Tests
    def test_encounter_class_traits(self):
        """Test that class traits influence encounter outcomes."""
        encounter = self.valid_scripted_encounters[0]
        outcome = encounter["outcomes"]["fight"]
        success_rate = outcome["success_rate"] + self.player_state["class"]["attributes"]["strength"]
        self.assertGreater(success_rate, 70, "Class traits did not affect success rate as expected.")

    def test_encounter_story_integration(self):
        """Test that encounter results affect the narrative."""
        encounter = self.valid_scripted_encounters[0]
        outcome = encounter["outcomes"]["flee"]
        result = process_encounter_result(self.player_state, outcome)
        self.assertTrue(result["escaped"], "Narrative progression did not reflect encounter outcome.")

    # Edge Case Tests
    def test_partial_scripted_encounter(self):
        """Test handling of partial scripted encounter data."""
        encounter = generate_scripted_encounter(self.partial_scripted_encounters, 1)
        self.assertIsNone(encounter, "System did not handle partial encounter data correctly.")

if __name__ == "__main__":
    unittest.main()

