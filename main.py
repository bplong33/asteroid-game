import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("""

____ ___ ____ ____ ___ _ _  _ ____       
[__   |  |__| |__/  |  | |\ | | __       
___]  |  |  | |  \  |  | | \| |__]       
                                         
____ ____ ___ ____ ____ ____ _ ___  ____ 
|__| [__   |  |___ |__/ |  | | |  \ [__  
|  | ___]  |  |___ |  \ |__| | |__/ ___] 

""")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # add groups to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        # update
        updatable.update(dt)

        for each in asteroids:
            if each.isColliding(player):
                print("Game over!")
                sys.exit(1)

            for shot in shots:
                if shot.isColliding(each):
                    shot.kill()
                    each.split()


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
