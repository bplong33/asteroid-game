import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print("""

____ ___ ____ ____ ___ _ _  _ ____       
[__   |  |__| |__/  |  | |\ | | __       
___]  |  |  | |  \  |  | | \| |__]       
                                         
____ ____ ___ ____ ____ ____ _ ___  ____ 
|__| [__   |  |___ |__/ |  | | |  \ [__  
|  | ___]  |  |___ |  \ |__| | |__/ ___] 

""")

    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (updatable, drawable, asteroids)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
