import traceback
import pygame
import sys
from ui import UIManager
from stage_manager import StageManager
from storyteller import load_story
from classes import ClassManager
from boss import initialize_boss
from logger import log_event, log_error
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def initialize_game():
    """Initialize the game components."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Story Smith")

    log_event("Initializing game systems...")
    stage_manager = StageManager()
    stage_manager.initialize_stage("start_stage")
    class_manager = ClassManager()
    ui_manager = UIManager(screen)
    ui_manager.initialize_ui()

    return screen, stage_manager, class_manager, ui_manager

def run_game():
    """Run the game."""
    try:
        screen, stage_manager, class_manager, ui_manager = initialize_game()
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen
            screen.fill((0, 0, 0))

            # Render stage and UI
            stage_manager.render_stage(screen)
            ui_manager.render_ui({})

            # Update the display
            pygame.display.flip()

            # Cap frame rate
            clock.tick(60)

    except Exception as e:
        error_details = traceback.format_exc()
        log_error(f"An error occurred:\n{error_details}")
        print(f"An error occurred:\n{error_details}")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    run_game()

