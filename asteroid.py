import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            delta_angle = random.uniform(20, 50)

            s1_velocity = self.velocity.rotate(delta_angle)
            s2_velocity = self.velocity.rotate(-delta_angle)

            new_r = self.radius - ASTEROID_MIN_RADIUS

            s1 = Asteroid(self.position[0], self.position[1], new_r)
            s2 = Asteroid(self.position[0], self.position[1], new_r)

            s1.velocity = s1_velocity * 1.2
            s2.velocity = s2_velocity * 1.2
