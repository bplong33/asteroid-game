import pygame
from constants import *

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
