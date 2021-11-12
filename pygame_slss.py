# PYGAME
# Olivia Yan
# Nov 9 2021

import pygame
pygame.init()
# define color used
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0,0)
GREEN = (0, 255,0)
BLUE = (0,0,255)

# define the size of the canvas
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"

def main()->None:
    """Driver of the Python script"""
    # create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)
    # create some local variables that describe the environment
    done =  False
    clock = pygame.time.Clock()
    # create the main logo
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((254, 250, 224))
        # draw bg
        pygame.draw.circle(screen, (221, 161, 94),(150,100), 70)
        pygame.draw.rect(screen, (96, 108, 56), (0,500, 800,100))

        for i in range(5): # draw five blocks
            pygame.draw.rect(screen, (40, 54, 24), (100+i*50, 300, 49, 49))
            pygame.draw.ellipse(screen, (255, 183, 3), (120+i*50, 270, 20,25))

        # draw ladder one
        for a in range(2):
            pygame.draw.rect(screen, (40, 54, 24), (102+a*33, 351, 7, 100))

        for i in range(5):
            pygame.draw.rect(screen, (40, 54, 24), (102, 355+i*20, 33,7))
        # draw second place
        for i in range(4):
            pygame.draw.rect(screen, (40, 54, 24), (550 + i * 50, 200, 49, 49))
            pygame.draw.ellipse(screen, (255, 183, 3), (570 + i * 50, 170, 20, 25))
        for a in range(2):
            pygame.draw.rect(screen, (40, 54, 24), (670 + a * 33, 250, 7, 100))

        for i in range(5):
            pygame.draw.rect(screen, (40, 54, 24), (670, 255 + i * 20, 33, 7))

        # draw the middle place
        for i in range(3):
            pygame.draw.rect(screen, (40, 54, 24), (300 + i * 50, 120, 49, 49))

        for a in range(2):
            pygame.draw.rect(screen, (40, 54, 24), (310 + a * 33, 170, 7, 50))

        for i in range(3):
            pygame.draw.rect(screen, (40, 54, 24), (310, 176 + i * 15, 33, 6))


        pygame.display.flip()
        clock.tick(75)
if __name__ == "__main__":
    main()