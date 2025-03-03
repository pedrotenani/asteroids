import pygame
from circleshape import CircleShape

class Shot(CircleShape, pygame.sprite.Sprite):
    containers = []

    def __init__(self, x, y, velocity):
        super().__init__(x, y, 5)  # Assuming a radius of 5 for the shot
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt