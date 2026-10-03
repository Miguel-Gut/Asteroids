#import data for player information
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
      super().__init__(x,y, PLAYER_RADIUS)
      self.rotation = 0
      #cooldown to prevent shoot minigunning (SPAM)
      self.player_cooldown = 0
    # Makes the players hitbox
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    # display the player object to the screen
    def draw (self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    #controls the rotation of player
    def rotate (self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if self.player_cooldown > 0:
            self.player_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            if self.player_cooldown > 0:
                pass
            else:
                self.player_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()

    #Will prevent player from being stuck
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    #calculates how the player shoots
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
