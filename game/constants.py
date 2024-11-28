import os
import pygame

# Base project root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # Resolves to the directory containing constants.py
ASSETS_PATH = os.path.join(PROJECT_ROOT, "../assets/")
CONFIG_PATH = os.path.join(ASSETS_PATH, "config/")
GRAPHICS_PATH = os.path.join(ASSETS_PATH, "graphics/")
SOUNDS_PATH = os.path.join(ASSETS_PATH, "sounds/")
LOGS_PATH = os.path.join(ASSETS_PATH, "logs/")

# System Fonts
pygame.font.init()  # Initialize font subsystem
UI_FONT = pygame.font.match_font("DejaVuSans")  # Try to find 'DejaVuSans' (or fallback to default sans-serif)
NARRATIVE_FONT = pygame.font.match_font("Ubuntu")  # Try 'Ubuntu' font
DECORATIVE_FONT = pygame.font.match_font("LiberationSerif")  # Try 'LiberationSerif'

# Graphics
PROPS_PATH = os.path.join(GRAPHICS_PATH, "props/")
BACKGROUNDS_PATH = os.path.join(GRAPHICS_PATH, "backgrounds/")
UI_GRAPHICS_PATH = os.path.join(GRAPHICS_PATH, "ui/")
ANIMATIONS_PATH = os.path.join(GRAPHICS_PATH, "animations/")
EFFECTS_PATH = os.path.join(GRAPHICS_PATH, "effects/")

# Sounds
EFFECTS_SOUNDS_PATH = os.path.join(SOUNDS_PATH, "effects/")
MUSIC_SOUNDS_PATH = os.path.join(SOUNDS_PATH, "music/")
AMBIANCE_SOUNDS_PATH = os.path.join(SOUNDS_PATH, "ambiance/")
UI_SOUNDS_PATH = os.path.join(SOUNDS_PATH, "ui/")

# Colors (RGB format)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

# Screen settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FRAME_RATE = 60  # Frames per second

# Gameplay settings
DEFAULT_DIFFICULTY = "normal"
PLAYER_MAX_HEALTH = 100
PLAYER_MAX_MANA = 50
ENEMY_RESPAWN_RATE = 30  # in seconds

# UI settings
UI_FONT_SIZE = 24
UI_BUTTON_COLOR = COLOR_BLUE
UI_BUTTON_HOVER_COLOR = (100, 100, 255)

# Debug settings
ENABLE_DEBUG_MODE = True
LOG_FILE_PATH = os.path.join(LOGS_PATH, "storysmith.log")

# Miscellaneous
DEFAULT_LANGUAGE = "en"

