from circleshape import CircleShape
from pygame import draw, Vector2
from constants import ASTEROID_MIN_RADIUS
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen) -> None:
        draw.circle(screen,
                           (255, 255, 255),
                           self.position,
                           self.radius, 
                           2)

    def update(self, dt) -> None:
        self.position += self.velocity*dt
        
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = uniform(20, 50)
        velocity_left = self.velocity.rotate(-split_angle)
        velocity_right = self.velocity.rotate(split_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        
        left_asteroid = Asteroid(self.position.x, self.position.y, radius)
        right_asteroid = Asteroid(self.position.x, self.position.y, radius)

        left_asteroid.velocity += velocity_left*1.2
        right_asteroid.velocity += velocity_right*1.2