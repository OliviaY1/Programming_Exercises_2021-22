# Pygame Boilerplate
# Author: Ubial
# 2021 Version


import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
BGCOLOUR = (100, 100, 255)

YELLOW = (246, 189, 96)
GREY = (247, 237, 226)
PINK = (245, 202, 195)
GREEN = (132, 165, 157)
PEACH = (242, 132, 130)


SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "<<Your Title Here>>"



class Dvdimage:
    """Represents a dadimage on screen

    Attributes:
        x, y: coordinates of top-left corner
        width: width of the rectangle in px
        height: height of the rectangle in px
        color: 3-tuple of (r,g,b)
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.width = 150
        self.height = 90
        self.color = PINK
        self.x_vel = 5
        self.y_vel = 3
    def rect(self) -> pygame.rect:
        return [(self.x, self.y), self.width, self.height]
    def update(self) -> None:
        # update the coordinates of x and y
        self.x += self.x_vel
        self.y += self.y_vel




def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()
    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        dvd_image.update()
        print(f"x:{dvd_image.x}, y:{dvd_image.y}")
        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BLACK)      # fill with bgcolor
        pygame.draw.rect(screen, dvd_image.color, dvd_image.rect())
        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()