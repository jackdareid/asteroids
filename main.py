import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player 
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Game init
    pygame.init()

    # Screen / frame specs
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_limiter = pygame.time.Clock()
    dt = 0.0

    # Player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add Player class to these groups
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Init player and field
    AsteroidField()
    player = Player(x, y)

    # Game loop
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Limit FPS to 60
        dt = frame_limiter.tick(60) / 1000

        updatable.update(dt)
        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()

        # Fill screen with black
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        # Refresh screen with display.flip()
        pygame.display.flip()


if __name__ == "__main__":
    main()
