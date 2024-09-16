from circleshape import CircleShape
from pygame import draw
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen) -> None:
        draw.circle(screen,
                    (255, 255, 255),
                    self.position,
                    self.radius, 
                    2)
        
    def update(self, dt) -> None:
        self.position += self.velocity*dt
    
    