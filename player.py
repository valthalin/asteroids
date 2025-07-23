from pygame import sprite, Vector2, draw, key, K_a, K_d, K_w, K_s, K_SPACE
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)

        self.rotation = 0
        self.fire_cooldown = PLAYER_SHOOT_COOLDOWN
        self.can_fire = True
    
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

        #Turn
        if keys[K_a]:
            self.rotate(-delta_time)
        if keys[K_d]:
            self.rotate(delta_time)

        #Move
        if keys[K_w]:
            self.move(delta_time)
        if keys[K_s]:
            self.move(-delta_time)
        
        #Shoot
        if keys[K_SPACE]:
            if self.can_fire:
                self.shoot(Shot, delta_time)
                self.can_fire = False
                self.fire_cooldown = PLAYER_SHOOT_COOLDOWN
        
        if False == self.can_fire:
            self.fire_cooldown -= delta_time

            if 0 >= self.fire_cooldown:
                self.can_fire = True


    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time
    
    def move(self, delta_time):
        forward = Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self, bullet, delta_time):
        new_shot = bullet(self.position.x, self.position.y, SHOT_RADIUS)
        new_shot.speed = PLAYER_SHOOT_SPEED
        new_shot.rotation = self.rotation
        # new_shot.target_list = Asteroid.containers[0]
        new_shot.move(delta_time)