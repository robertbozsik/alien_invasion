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

        # create the screen as fullscreen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Set the title of the Pygame window (default: "pygame window")
        pygame.display.set_caption("Alien Invasion")

        # initialize the ship object
        # the self argument here refers to the current instance of AlienInvasion
        self.ship = Ship(self)

    # helper methods
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        # if the key pressed is the right arrow key
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # if the key pressed is the left arrow key
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        # if the key released is the right arrow key
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # if the key released is the left arrow key
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # a helper method does work inside a class but isn't meant to be called through an instance
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # when the player clicks the game window's close button
            if event.type == pygame.QUIT:
                # exit the game
                sys.exit()

            # each keypress is registered as a KEYDOWN event
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # each key release is registered as a KEYUP event
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

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
            self.ship.update()
            self._update_screen()


if __name__ == "__main__":
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
