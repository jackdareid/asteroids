import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    # Prints 
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game init
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_limiter = pygame.time.Clock()
    dt = 0.0

    # Game loop
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass

        # Fill screen with black
        screen.fill("black")

        # Refresh screen with display.flip()
        pygame.display.flip()

        # Limit FPS to 60
        dt = frame_limiter.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()
