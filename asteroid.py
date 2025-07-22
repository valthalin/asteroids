from circleshape import CircleShape
from constants import ASTEROID_SPEED, ASTEROID_WIDTH
from pygame import Vector2, draw

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.width = ASTEROID_WIDTH
        self.rotation = 0
    
    def draw(self, screen):
        draw.circle(screen, "white", self.position, self.radius, self.width)

    def update(self, delta_time):
        self.move(delta_time)

    def move(self, delta_time):
        forward = Vector2(0, 1).rotate(self.rotation)
        self.position += forward * ASTEROID_SPEED * delta_time