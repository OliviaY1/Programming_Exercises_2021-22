# Pygame- DVD IMAGE
# Author: OY
# 2021 Version
import random

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
color_pick = [YELLOW, GREY, PINK, GREEN, PEACH]


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
        self.x_vel = 4
        self.y_vel = 2
        self.img = pygame.image.load("./images/dvdimage.png")
    def rect(self) -> pygame.rect:
        return [self.x, self.y, self.width, self.height]
    def update(self) -> None:
        # update the coordinates of x and y
        self.x += self.x_vel
        self.y += self.y_vel
        ran = random.randint(0,4)
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
            self.x_vel = - self.x_vel
            self.color = color_pick[ran]
        elif self.x < 0:
            self.x = 0
            self.x_vel = -self.x_vel
            self.color = color_pick[ran]
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            self.y_vel = -self.y_vel
            self.color = color_pick[ran]
        elif self.y < 0:
            self.y = 0
            self.y_vel = - self.y_vel
            self.color = color_pick[ran]






def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()
    # import bg image
    bg_image = pygame.image.load('./images/backgroundimage.jpg')
    bg_image = pygame.transform.scale(bg_image, (990, 600))

    # ----------- MAIN LOOP
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        dvd_image.update()
        print(f"x:{dvd_image.x}, y:{dvd_image.y}")

        # ----------- DRAW THE ENVIRONMENT
        # Draw the bg image
        screen.blit(bg_image, (0,0))

        # Draw the rectangle
        pygame.draw.rect(screen, dvd_image.color, dvd_image.rect())

        # Draw the image "dvd" on the rectangle
        dvd_image.img = pygame.transform.scale(dvd_image.img, (150, 160))
        screen.blit(dvd_image.img, (dvd_image.x-3, dvd_image.y-40))

        # ------------ Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()