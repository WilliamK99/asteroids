# this allows us to use code from the open-source pygame library throughout the file
import pygame
from constants import * 

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill screen with all black
        screen.fill((0, 0, 0))

        # Refresh the screen 
        pygame.display.flip()

if __name__ == "__main__":
    main()