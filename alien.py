import pygame


class Alien:
    """Represents one alien in the fleet."""

    def __init__(self, game, x, y):
        """Load the alien image and place it on the screen."""
        self.screen = game.screen

        self.image = pygame.image.load("Images/alien.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self, direction, speed):
        """Move the alien left or right."""
        self.rect.x += speed * direction

    def draw(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)