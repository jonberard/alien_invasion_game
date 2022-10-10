import sys
import pygame
from settings import Settings


# above imports and contains the functionality we need to build on.
# sys module contains the exit functionality we need when player quits


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # creates display window in px
        # imports the screen width and height from settings file
        #  surface variable - part of screen in PyGame where game element can be displayed
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        #  This method controls the whole game.
        #  Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                #  an event is an action the user performs while playing the game. This event loop listens for events.
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.

            # make the most recently drawn screen visible. draws and empty new screen on each loop pass.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
