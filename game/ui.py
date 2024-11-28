import pygame
from constants import COLOR_WHITE, COLOR_RED, UI_FONT, UI_FONT_SIZE

class UIManager:
    def __init__(self, screen):
        """Initialize UI Manager with screen reference."""
        self.screen = screen
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

    def initialize_ui(self):
        """Set up UI elements and load assets."""
        self.health_gauge = {"current": 100, "max": 100}
        self.mana_gauge = {"current": 50, "max": 50}
        self.dialogue_box = {"active": False, "text": ""}
        print("UI Initialized")

    def render_ui(self, game_state):
        """Render all UI components."""
        # Clear only the UI region
        self.screen.fill((0, 0, 0), (0, 0, 300, 80))  # Clear the top-left UI area

        # Render health and mana gauges
        self.render_gauges()

        # Render dialogue box if active
        if self.dialogue_box["active"]:
            self.render_dialogue_box(self.dialogue_box["text"])

    def update_ui(self, game_state):
        """Update UI components based on game state."""
        player = game_state.get("player")
        if player:
            self.health_gauge["current"] = max(0, min(self.health_gauge["max"], player["health"]))
            self.mana_gauge["current"] = max(0, min(self.mana_gauge["max"], player["mana"]))

    def handle_ui_events(self, event, game_state):
        """Handle player inputs for interacting with the UI."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.dialogue_box["active"]:
                self.dialogue_box["active"] = False

    def render_gauges(self):
        """Render health and mana gauges."""
        # Render health gauge (red bar with white border)
        pygame.draw.rect(self.screen, COLOR_RED, (10, 10, self.health_gauge["current"] * 2, 20))
        pygame.draw.rect(self.screen, COLOR_WHITE, (10, 10, self.health_gauge["max"] * 2, 20), 2)

        # Render mana gauge (red bar with white border)
        pygame.draw.rect(self.screen, COLOR_RED, (10, 40, self.mana_gauge["current"] * 2, 20))
        pygame.draw.rect(self.screen, COLOR_WHITE, (10, 40, self.mana_gauge["max"] * 2, 20), 2)

    def render_dialogue_box(self, text):
        """Render a dialogue box with the given text."""
        # Render a white box for dialogue
        pygame.draw.rect(self.screen, COLOR_WHITE, (50, 400, 800, 200))
        dialogue_text = self.font.render(text, True, COLOR_RED)
        self.screen.blit(dialogue_text, (60, 420))

