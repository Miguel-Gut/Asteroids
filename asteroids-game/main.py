#still works? able to print wanted results but still shows an error
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from logger import log_state
from player import Player

def main():
    pygame.init()
    #makes a clock
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #makes the player
    player = Player(SCREEN_WIDTH / 2 ,SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            #will check if the user pressed the X to close the window and closes it
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        #sets the delta time
        dt = clock.tick(60) / 1000
        player.update(dt)

    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
