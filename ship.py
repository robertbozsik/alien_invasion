import pygame


class Ship:
    """A class to manage the ship."""

    # two parameters: the self reference and a reference to the current instance of the AlienInvasion class
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("./images/ship.bmp")
        self.image_rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # the default place of the image is at the top left corner
        self.image_rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flags."""
        if self.moving_right:
            self.image_rect.x += 1
        # if we used "elif" for motion to the left, the right arrow key would always have priority
        if self.moving_left:
            self.image_rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)
