#still works? able to print wanted results but still shows an error
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
#force sounds into the game
import os

def main():
    pygame.init()
    #mixer for game
    os.environ["SDL_AUDIODRIVER"] = "pulseaudio"
    pygame.mixer.init()
    #makes a clock
    clock = pygame.time.Clock()
    dt = 0.0
    #will make the score value and track it
    score = 0
    #Colers
    white = (255,255,255)
    black = (0,0,0)
    #score font and size
    font = pygame.font.Font('freesansbold.ttf', 20)
    #sounds for game
    explosion_sound = pygame.mixer.Sound("explosion.wav")
    die_sound = pygame.mixer.Sound("hitHurt.wav")
    #screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #makes groups to manage the diffrent variables
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
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
        display_score = font.render("Score: "+ str(score), True, white, black)
        screen.blit(display_score, (10,10))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print ("Game over!")
                die_sound.play()
                sys.exit()
            #will check if a shot has colided with an asteroid.
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    #adds points to the score
                    score += 10
                    explosion_sound.play()



        #sets the delta time limit to 60 FPS
        dt = clock.tick(60) / 1000


    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
