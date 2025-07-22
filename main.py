import pygame
from constants import *
import player

# uv run main.py

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player1 = player.Player(x,y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((25,25,25))
        player1.draw(screen)

        pygame.display.flip()
        delta = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
