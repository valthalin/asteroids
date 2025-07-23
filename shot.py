from pygame import sprite, Vector2, draw
from constants import SHOT_RADIUS, SHOT_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.width = SHOT_WIDTH
        self.speed = 0
        self.target_list = []
        self.life_time = 3

    def draw(self, screen):
        draw.circle(screen, "red", self.position, self.radius, self.width)

    def update(self, delta_time):
        self.move(delta_time)

        self.life_time -= delta_time
        self.radius -= delta_time * 4

        if 0 >= self.life_time or 0.4 >= self.radius:
            print("Timed out!")
            self.die()

    def move(self, delta_time):
        forward = Vector2(0, 1).rotate(self.rotation)
        self.position += (forward * self.speed * delta_time)