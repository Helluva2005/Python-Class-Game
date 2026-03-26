import sys
import random
import pygame

from ship import Ship
from bullet import Bullet
from alien import Alien
from alien_bullet import AlienBullet


class AlienInvasion:
    """Main class for the Alien Invasion game."""

    def __init__(self):
        """Set up the game window and starting values."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.big_font = pygame.font.SysFont(None, 72)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (66, 135, 245)

        self.reset_game()

    def reset_game(self):
        """Reset the game values for a new round."""
        self.ship = Ship(self)
        self.bullets = []
        self.alien_bullets = []
        self.aliens = []

        self.alien_direction = 1
        self.alien_speed = 2
        self.drop_speed = 20

        self.lives = 3
        self.score = 0
        self.game_active = True

        self.create_fleet()

    def create_fleet(self):
        """Create rows of aliens."""
        alien_width = 70
        alien_height = 70
        spacing_x = 40
        spacing_y = 30

        start_x = 100
        start_y = 60

        rows = 3
        cols = 8

        for row in range(rows):
            for col in range(cols):
                x = start_x + col * (alien_width + spacing_x)
                y = start_y + row * (alien_height + spacing_y)
                alien = Alien(self, x, y)
                self.aliens.append(alien)

    def run_game(self):
        """Run the main game loop."""
        while True:
            self.check_events()

            if self.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_alien_bullets()
                self.update_aliens()
                self.alien_fire()

            self.update_screen()

    def check_events(self):
        """Watch for keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE and self.game_active:
                    self.fire_bullet()
                elif event.key == pygame.K_r and not self.game_active:
                    self.reset_game()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def fire_bullet(self):
        """Create a new bullet and add it to the list."""
        new_bullet = Bullet(self)
        self.bullets.append(new_bullet)

    def alien_fire(self):
        """Randomly let one alien fire a bullet."""
        if self.aliens and random.randint(1, 60) == 1:
            shooter = random.choice(self.aliens)
            self.alien_bullets.append(AlienBullet(self, shooter))

    def update_bullets(self):
        """Update player bullets and check hits."""
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.check_bullet_alien_collisions()

    def update_alien_bullets(self):
        """Update alien bullets and check if they hit the ship."""
        for bullet in self.alien_bullets[:]:
            bullet.update()

            if bullet.rect.top >= self.screen.get_rect().bottom:
                self.alien_bullets.remove(bullet)
            elif bullet.rect.colliderect(self.ship.rect):
                self.alien_bullets.remove(bullet)
                self.ship_hit()

    def ship_hit(self):
        """Handle the ship being hit by an alien bullet."""
        self.lives -= 1

        if self.lives <= 0:
            self.game_active = False

    def check_bullet_alien_collisions(self):
        """Remove bullets and aliens that collide."""
        for bullet in self.bullets[:]:
            for alien in self.aliens[:]:
                if bullet.rect.colliderect(alien.rect):
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if alien in self.aliens:
                        self.aliens.remove(alien)
                        self.score += 10
                    break

        if not self.aliens:
            self.game_active = False

    def update_aliens(self):
        """Move the alien fleet."""
        if not self.aliens:
            return

        move_down = False

        for alien in self.aliens:
            if alien.rect.right >= self.screen.get_rect().right or alien.rect.left <= 0:
                move_down = True
                break

        if move_down:
            self.alien_direction *= -1
            for alien in self.aliens:
                alien.rect.y += self.drop_speed

        for alien in self.aliens:
            alien.update(self.alien_direction, self.alien_speed)

    def update_screen(self):
        """Redraw the screen each frame."""
        self.screen.fill(self.bg_color)
        self.ship.draw()

        for alien in self.aliens:
            alien.draw()

        for bullet in self.bullets:
            bullet.draw()

        for bullet in self.alien_bullets:
            bullet.draw()

        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))

        self.screen.blit(lives_text, (20, 20))
        self.screen.blit(score_text, (20, 55))

        if not self.game_active:
            if self.lives <= 0:
                message = "Game Over - Press R to Restart"
            else:
                message = "You Win - Press R to Restart"

            end_text = self.big_font.render(message, True, (255, 255, 255))
            end_rect = end_text.get_rect(center=(600, 400))
            self.screen.blit(end_text, end_rect)

        pygame.display.flip()
        self.clock.tick(60)


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()