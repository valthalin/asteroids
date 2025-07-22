from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from pygame import Vector2, draw, key, K_a, K_d, K_w, K_s
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)

        self.rotation = 0
    
    # in the player class
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
   
    def draw(self, screen):
        # sub-classes must override
        draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, delta_time):
        keys = key.get_pressed()

        if keys[K_a]:
            self.rotate(-delta_time)
        if keys[K_d]:
            self.rotate(delta_time)

        if keys[K_w]:
            self.move(delta_time)
        if keys[K_s]:
            self.move(-delta_time)
        
    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time
    
    def move(self, delta_time):
        forward = Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time