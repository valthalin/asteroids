from pygame import Vector2, draw
from random import uniform
from constants import ASTEROID_SPEED, ASTEROID_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.width = ASTEROID_WIDTH
        self.rotation = 0
        self.color = "white"
        self.life_time = 6

    def draw(self, screen):
        self.set_color()
        draw.circle(screen, self.color, self.position, self.radius, self.width)

    def update(self, delta_time):
        self.move(delta_time)
        self.life_time -= delta_time

        if 0 >= self.life_time or 0.4 >= self.radius:
            print("Timed out!")
            self.die()

    def move(self, delta_time):
        # forward = Vector2(0, 1).rotate(self.rotation)
        # self.position += forward * ASTEROID_SPEED * delta_time
        self.position += (self.velocity * ASTEROID_SPEED) * delta_time
 
    def set_color(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            self.color = "red"
        elif ASTEROID_MIN_RADIUS < self.radius and self.radius < ASTEROID_MAX_RADIUS:
            self.color = "gray"
        elif self.radius == ASTEROID_MAX_RADIUS:
            self.color = "white"

    def spawn_fragment(self, div_angle):
        fragment = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        fragment.velocity = self.velocity.rotate(div_angle) * 1.2

        return fragment
   
    def split(self):
        self.die()
        if self.radius > ASTEROID_MIN_RADIUS:
            rangle = uniform(20, 50)
            frag_a = self.spawn_fragment(rangle)
            frag_b = self.spawn_fragment(-rangle)