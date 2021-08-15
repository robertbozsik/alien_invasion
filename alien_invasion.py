import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # Initialize the background settings that Pygame needs to work properly.
        pygame.init()
        self.settings = Settings()

        # create the screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set the title of the Pygame window (default: "pygame window")
        pygame.display.set_caption("Alien Invasion")

        # initialize the ship object
        # the self argument here refers to the current instance of AlienInvasion
        self.ship = Ship(self)

    # a helper method does work inside a class but isn't meant to be called through an instance
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # when the player clicks the game window's close button
            if event.type == pygame.QUIT:
                # exit the game
                sys.exit()

    # a single leading underscore indicates a helper method
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # fill the screen with the background color
        self.screen.fill(self.settings.bg_color)

        # draw the ship on the screen
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()


if __name__ == "__main__":
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
