from pygame import sprite, Vector2

# Base class for game objects
class CircleShape(sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, other):
        result = False
        range = Vector2.distance_to(other.position, self.position)

        if range < (self.radius + other.radius):
            print(f"Game Over!")
            result = True

        return result