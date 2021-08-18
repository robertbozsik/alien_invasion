import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # set the screen fullscreen
        # self.fullscreen = pygame.FULLSCREEN
        # self.screen = pygame.display.set_mode((0, 0), self.fullscreen)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # Set the title of the Pygame window (default: "pygame window")
        pygame.display.set_caption("Alien Invasion")

        # initialize the ship object
        # the self argument here refers to the current instance of AlienInvasion
        self.ship = Ship(self)

        # create a group (list) of bullets variable
        self.bullets = pygame.sprite.Group()

        # create a group (list) of aliens attribute
        self.aliens = pygame.sprite.Group()
        # create the fleet of aliens
        self._create_fleet()

    # helper methods
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            # initialize a bullet object
            new_bullet = Bullet(self)
            # add() is a method written specifically for Pygame groups
            self.bullets.add(new_bullet)

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

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

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width = alien.rect.width  # e.g. 50 px
        # available_space_x = self.screen.get_rect().width - (2 * alien_width)
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Crate the first row of aliens
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row
            alien = Alien(self)
            alien.x = alien_width + ((2 * alien_width) * alien_number)
            alien.rect.x = alien.x
            self.aliens.add(alien)

    # a single leading underscore indicates a helper method
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # fill the screen with the background color
        self.screen.fill(self.settings.bg_color)

        # draw the ship on the screen
        self.ship.blitme()

        # draw the bullets on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # draw the aliens group on the screen
        # When you call draw() on a group, Pygame draws each element in the group
        # at the position defined by its rect attribute. The draw() method requires
        # one argument: a surface to which to draw the elements from the group.
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:  # 0 is same as self.screen.get_rect().top
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()


if __name__ == "__main__":
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
