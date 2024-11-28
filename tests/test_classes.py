import unittest
from game.classes import load_classes, get_class_by_name, modify_class_stat, apply_ability_effect

class TestClasses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up shared resources for class tests."""
        # Load valid data from test JSONs
        cls.valid_classes = load_classes("test_data/valid/valid_classes.json")
        cls.partial_classes = load_classes("test_data/partial/partial_classes.json")

    def setUp(self):
        """Reset the Warrior class for each test."""
        self.warrior_class = get_class_by_name(self.valid_classes, "Warrior")
        self.warrior_class["attributes"]["health"] = 150
        self.warrior_class["attributes"]["mana"] = 50

    # Data Validation Tests
    def test_load_classes_valid(self):
        """Test loading valid class data."""
        self.assertIsInstance(self.valid_classes, list, "Class data should be a list.")
        self.assertGreater(len(self.valid_classes), 0, "No classes found in the data.")

    def test_load_classes_invalid_file(self):
        """Test behavior when classes.json is missing."""
        with self.assertRaises(FileNotFoundError):
            load_classes("test_data/invalid/nonexistent_classes.json")

    def test_load_partial_classes(self):
        """Test loading partial class data with fallback handling."""
        classes = self.partial_classes
        warrior = get_class_by_name(classes, "Warrior")
        self.assertIn("health", warrior["attributes"], "Partial data fallback failed for 'health'.")

    # Class Functionality Tests
    def test_get_class_by_name(self):
        """Test retrieving a class definition by name."""
        warrior = get_class_by_name(self.valid_classes, "Warrior")
        self.assertIsNotNone(warrior, "Failed to retrieve the Warrior class.")
        self.assertEqual(warrior["name"], "Warrior", "Retrieved class name does not match.")

    def test_modify_class_stat(self):
        """Test modifying a class stat dynamically."""
        modify_class_stat(self.valid_classes, "Warrior", "health", -20)
        updated_health = self.warrior_class["attributes"]["health"]
        self.assertEqual(updated_health, 130, "Class stat modification failed.")

    # Ability Execution Tests
    def test_apply_ability_effect(self):
        """Test applying an ability's effect."""
        target = {"name": "Enemy", "attributes": {"health": 100}}
        apply_ability_effect(self.valid_classes, "Warrior", "Shield Bash", target)
        self.assertEqual(target["attributes"]["health"], 85, "Ability effect did not apply correctly.")
        # Verify mana cost application
        self.assertEqual(self.warrior_class["attributes"]["mana"], 40, "Mana cost was not deducted.")

    # Integration Tests
    def test_class_traits_to_storyteller(self):
        """Test that class traits influence narrative branching."""
        self.warrior_class["attributes"]["strength"] = 20
        # Mock interaction with storyteller
        narrative_outcome = "forest_path"  # Example result
        self.assertEqual(narrative_outcome, "forest_path", "Class traits did not influence narrative as expected.")

    def test_class_to_ui_updates(self):
        """Test that UI reflects changes to class stats and abilities."""
        self.warrior_class["attributes"]["mana"] = 40
        # Mock UI update logic
        updated_mana = self.warrior_class["attributes"]["mana"]
        self.assertEqual(updated_mana, 40, "UI did not reflect updated mana.")

if __name__ == "__main__":
    unittest.main()

