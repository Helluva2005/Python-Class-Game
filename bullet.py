import pygame


class Bullet:
    """A class to manage bullets fired from the ship."""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        self.screen = game.screen
        self.color = (255, 255, 255)

        self.rect = pygame.Rect(0, 0, 6, 18)
        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)
        self.speed = 7

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)