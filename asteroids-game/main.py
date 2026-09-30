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
    #makes two groups to manage the diffrent variables
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    #makes the player
    player = Player(SCREEN_WIDTH / 2 ,SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            #will check if the user pressed the X to close the window and closes it
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        #sets the delta time limit to 60 FPS
        dt = clock.tick(60) / 1000


    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
