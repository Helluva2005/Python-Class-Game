import pygame


class Ship:
    """Represents the player's ship."""

    def __init__(self, game):
        """Load the ship image and place it at the bottom center."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("Images/ship.png")
        self.image = pygame.transform.scale(self.image, (90, 120))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 40

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        self.speed = 5

    def update(self):
        """Move the ship left or right."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        self.rect.x = self.x

    def draw(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)