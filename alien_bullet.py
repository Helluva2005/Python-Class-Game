import pygame


class AlienBullet:
    """Represents a bullet fired by an alien."""

    def __init__(self, game, alien):
        """Create a bullet at the alien's position."""
        self.screen = game.screen
        self.color = (255, 80, 80)

        self.rect = pygame.Rect(0, 0, 6, 18)
        self.rect.midbottom = alien.rect.midbottom

        self.y = float(self.rect.y)
        self.speed = 4

    def update(self):
        """Move the bullet downward."""
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)