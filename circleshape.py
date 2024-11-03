import pygame

class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def check_collision(self, circle):
        dr = self.position.distance_to(circle.position)

        r1 = self.radius
        r2 = circle.radius

        if dr > (r1 + r2):
            return False
        else:
            return True

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
