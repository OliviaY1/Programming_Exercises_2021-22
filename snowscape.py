# Pygame SNOWSCAPE
# Author: OY
# 2021 Version
import random

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "OY's Snowscape"

class Snow:
    def __init__(self):
        self.radius = 5
        speed = random.randint(1,5)
        self.fall_speed = speed
        x = random.randint(1, 800)
        self.x = x
        self.y = SCREEN_HEIGHT
    def update(self)->None:
        self.y += self.fall_speed
        if self.y > self.radius + SCREEN_HEIGHT:
            return None



def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_snowflakes = 230
    snowflakes = []
    for i in range(num_snowflakes - 150):
        close_snowflake = Snow()
        close_snowflake.size = random.choice([4, 5, 6])
        close_snowflake.y_vel = random.choice([1, 2])
        snowflakes.append(close_snowflake)
    for i in range(num_snowflakes - 100):
        close_snowflake = Snow()
        close_snowflake.size = random.choice([3, 4])
        close_snowflake.y_vel = random.choice([2, 3])
        snowflakes.append(close_snowflake)
        # Create snowflakes in background
    for i in range(num_snowflakes):
        snowflakes.append(Snow())
    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        for snow in snowflakes:
            snow.update()
        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor
        # Draw the snow


        for snow in snowflakes:
            pygame.draw.circle(screen, WHITE, (snow.x, snow.y), snow.radius)
        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()