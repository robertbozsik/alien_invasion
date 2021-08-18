from typing import ClassVar
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""

        # inheritance and screen attribute set
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width  # self.rect.x = 50
        self.rect.y = self.rect.width  # self.rect.y = 60

        # Store the alien's exact (decimal value) horizontal position
        self.x = float(self.rect.x)
