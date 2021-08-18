import pygame


class Ship:
    """A class to manage the ship."""

    # two parameters: the self reference and a reference to the current instance of the AlienInvasion class
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        # set the screen and screen_rect (rectangle) equal to the game screen.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # set the setting equal to the game settings
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("./images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flags.
        It means moving the ship left or right."""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # if we used "elif" for motion to the left, the right arrow key would always have priority
        # self.screen_rect.left is also equal to the 0th horizonlat pixel:
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # # Update the rect object's position
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
