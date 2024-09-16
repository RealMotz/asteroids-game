import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def update_all(group: pygame.sprite.Group, dt: float):
    for obj in group:
        obj.update(dt)
        
def draw_all(group: pygame.sprite.Group, screen: pygame.Surface):
    for obj in group:
        obj.draw(screen)
        
def collision_occurred(group: pygame.sprite.Group, player: Player):
    for obj in group:
        if obj.isCollidingWith(player):
            return True
    return False

def destroy_shot_asteriods(asteriods: pygame.sprite.Group, shots: pygame.sprite.Group):
    for shot in shots:
        for asteroid in asteriods:
            if shot.isCollidingWith(asteroid):
                shot.kill()
                asteroid.split()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteriods, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        update_all(updatable, dt)

        if (collision_occurred(asteriods, player)):
            print("Game Over!")
            sys.exit()
    
        destroy_shot_asteriods(asteriods, shots)

        draw_all(drawable, screen)

        pygame.display.flip()
        timeElapsed = clock.tick(60)
        dt = timeElapsed/1000

if __name__ == "__main__":
    main()
