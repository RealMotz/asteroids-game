from pygame import sprite, Vector2

# Base class for game objects
class CircleShape(sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius
        
    def isCollidingWith(self, other : 'CircleShape') -> bool:
        dist = self.position.distance_to(other.position)
        return dist < (self.radius + other.radius)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass