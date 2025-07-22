from constants import *
from sys import exit
import pygame
#from pygame import display, time, sprite, QUIT
#event is local and not importable
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# uv run main.py

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Environment Setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    #New Empty Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    players = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    #Group Assignments
    Player.containers = (players, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    #Actor initialization
    player = Player(x, y, PLAYER_RADIUS)
    #asteroid = Asteroid(x, y, ASTEROID_RADIUS)
    asteroidfield = AsteroidField()


    #Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Initial Frame Setup
        screen.fill((25,25,25))

        #Update Calls
        updatable.update(delta_time)
        
        #Draw Calls
        for art in drawable:
            art.draw(screen)
        
        for rock in asteroids:
            if player.collision(rock):
                exit(0)

        #Update Frame Stats
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
