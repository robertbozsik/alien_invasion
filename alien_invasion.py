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

        # Available in all methods in the class
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set the title of the Pygame window (default: "pygame window")
        pygame.display.set_caption("Alien Invasion")

        # initialize the ship object
        # self.ship_image = pygame.image.load("./images/ship.bmp")
        # self.ship_rect = self.ship_image.get_rect()
        # self.ship_rect.midbottom = self.screen.get_rect().midbottom
        self.ship = Ship(self)

        # Set the background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Whatch for keyboard and mouse events.
            for event in pygame.event.get():
                # when the player clicks the game window's close button
                if event.type == pygame.QUIT:
                    # exit the game
                    sys.exit()

            # fill the screen with the background color
            # this will redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # draw the ship on the screen
            # self.screen.blit(self.ship_image, self.ship_rect)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
