#controls hot the player shoots
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS
import pygame
class Shot(CircleShape):
    def __init__(self, x: float, y: float)-> None:
        super().__init__(x, y, SHOT_RADIUS)
    # makes the shot
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    #makes the shot move
    def update(self, dt):
        self.position += self.velocity * dt
