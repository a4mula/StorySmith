import unittest
from game.utils import load_json, save_json, calculate_damage, random_choice, flatten_nested_dict

class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for utility function tests."""
        cls.sample_valid_json = "test_data/valid/valid_settings.json"
        cls.sample_invalid_json = "test_data/invalid/invalid_settings.json"
        cls.sample_output_file = "test_data/temp/output.json"

    # File Handling Tests
    def test_load_json_valid(self):
        """Test loading a valid JSON file."""
        data = load_json(self.sample_valid_json)
        self.assertIsInstance(data, dict, "Loaded JSON data should be a dictionary.")
        self.assertIn("resolution", data, "Key 'resolution' not found in loaded JSON data.")

    def test_load_json_invalid(self):
        """Test loading an invalid JSON file."""
        with self.assertRaises(ValueError, msg="Invalid JSON file should raise ValueError."):
            load_json(self.sample_invalid_json)

    def test_save_json(self):
        """Test saving data to a JSON file."""
        data = {"key": "value"}
        save_json(data, self.sample_output_file)
        loaded_data = load_json(self.sample_output_file)
        self.assertEqual(data, loaded_data, "Saved JSON data does not match the original.")

    # Math and Logic Tests
    def test_calculate_damage(self):
        """Test damage calculation logic."""
        attacker = {"strength": 10}
        defender = {"defense": 5}
        damage = calculate_damage(attacker, defender)
        self.assertEqual(damage, 5, "Damage calculation failed.")

    def test_random_choice(self):
        """Test random choice function."""
        options = ["option1", "option2", "option3"]
        choice = random_choice(options)
        self.assertIn(choice, options, "Random choice is not one of the expected options.")

    # Data Processing Tests
    def test_flatten_nested_dict(self):
        """Test flattening of a nested dictionary."""
        nested_dict = {"a": {"b": {"c": 1}}, "d": 2}
        flattened = flatten_nested_dict(nested_dict)
        self.assertEqual(flattened, {"a.b.c": 1, "d": 2}, "Flattened dictionary does not match expected output.")

    # Error Handling Tests
    def test_load_json_missing_file(self):
        """Test behavior when a JSON file is missing."""
        with self.assertRaises(FileNotFoundError, msg="Missing JSON file should raise FileNotFoundError."):
            load_json("nonexistent_file.json")

    def test_calculate_damage_invalid_inputs(self):
        """Test damage calculation with invalid inputs."""
        attacker = {"strength": "invalid"}
        defender = {"defense": 5}
        with self.assertRaises(TypeError, msg="Invalid inputs should raise TypeError in calculate_damage."):
            calculate_damage(attacker, defender)

if __name__ == "__main__":
    unittest.main()

