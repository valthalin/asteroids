import pygame
from sys import exit
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField


## TODO
"""

    Add a scoring system
    Implement multiple lives and respawning
    Add an explosion effect for the asteroids
    Add acceleration to the player movement
    Make the objects wrap around the screen instead of disappearing
    Add a background image
    Create different weapon types
    Make the asteroids lumpy instead of perfectly round
    Make the ship have a triangular hit box instead of a circular one
    Add a shield power-up
    Add a speed power-up
    Add bombs that can be dropped

"""
# uv run main.py
def exit_app():
    exit(0)


def collsions(collider_list, collisions_list):
    result = []
    for collider in collider_list:
        for collision in collisions_list:
            if collider.collision_check(collision):
                result.append((collider, collision))
    
    return result


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
    shots = pygame.sprite.Group()


    #Group Assignments
    Player.containers = (players, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


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

        #Collision Calls
        shot_result = collsions(shots, asteroids)
        if 0 < len(shot_result):
            for hit in shot_result:
                hit[0].die()
                if Asteroid == type(hit[1]):
                    hit[1].split()
                else:
                    hit[1].die()

        
        #Player Collisions v Asteroid
        player_result = collsions(players, asteroids)
        if 0 < len(player_result):
            print("GAME OVER!")
            exit_app()

        print(f"Asteroids in play: {len(asteroids)}")

        #Update Frame Stats
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
