#still works? able to print wanted results but still shows an error
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from logger import log_state

def main():
    pygame.init()
    #makes a clock
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            #will check if the user pressed the X to close the window and closes it
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        #sets the delta time
        dt = clock.tick(60) / 1000
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
