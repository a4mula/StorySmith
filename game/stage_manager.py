import os
import json
import pygame
from constants import CONFIG_PATH

class StageManager:
    def __init__(self, file_path=None):
        """Initialize the Stage Manager."""
        self.file_path = file_path or os.path.join(CONFIG_PATH, "stages.json")
        self.stages = self.load_stages(self.file_path)
        self.current_stage = None
        self.layers = {"background": [], "midground": [], "foreground": []}

    def load_stages(self, file_path):
        """Load and validate stage configurations from a JSON file."""
        try:
            with open(file_path, "r") as file:
                stages = json.load(file)
            return stages
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading stages: {e}")
            return {}

    def initialize_stage(self, stage_name):
        """Set up a stage by name."""
        stage_config = self.stages.get(stage_name)
        if not stage_config:
            raise ValueError(f"Stage {stage_name} not found.")

        # Reset layers
        self.current_stage = stage_config
        self.layers = {"background": [], "midground": [], "foreground": []}

        # Populate layers
        self.populate_stage(stage_config)

    def populate_stage(self, stage_config):
        """Populate the stage layers."""
        for layer_name, items in stage_config.get("layers", {}).items():
            if not isinstance(items, list):
                continue
            for item in items:
                if isinstance(item, str):
                    self.layers[layer_name].append(item)

    def render_stage(self, screen):
        """Render all stage layers."""
        if not self.current_stage:
            return

        # Clear the stage before rendering
        screen.fill((0, 0, 0))  # Black background

        for layer_name, items in self.layers.items():
            y_offset = {"background": 50, "midground": 150, "foreground": 250}.get(layer_name, 0)
            for index, item in enumerate(items):
                color = (50 * (index + 1), 50 * (index + 2), 50 * (index + 3))
                placeholder_surface = pygame.Surface((100, 100))  # Placeholder 100x100 rectangle
                placeholder_surface.fill(color)

                position = (index * 120, y_offset)
                screen.blit(placeholder_surface, position)

