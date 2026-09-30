#this file holds the variables around asteroids
from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
   #makes the shape and attributes of the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    #sets how the asteroids move
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
