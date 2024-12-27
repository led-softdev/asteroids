import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SCALE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid = pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        left = self.velocity.rotate(new_angle)
        right = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        left_roid = Asteroid(self.position.x, self.position.y, new_radius)
        left_roid.velocity = left * ASTEROID_SCALE

        right_roid = Asteroid(self.position.x, self.position.y, new_radius)
        right_roid.velocity = right * ASTEROID_SCALE