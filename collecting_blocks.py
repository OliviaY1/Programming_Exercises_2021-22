# Collecting Blocks Example
# Author: oy
# Nov 25


import random
import time
import pygame


pygame.init()

WHITE =     (255, 255, 255)
BLACK =     (  0,   0,   0)
RED   =     (255,   0,   0)
GREEN =     (  0, 255,   0)
BLUE  =     (  0,   0, 255)
ETON_BLUE = (135, 187, 162)
RAD_RED =   (255,  56, 100)
BLK_CHOCOLATE = (25, 17, 2)

BGCOLOUR =  WHITE

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Collecing Blocks"


class Player(pygame.sprite.Sprite):
    """Describes a player object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
    """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.image.load("./images/smb_mario.png") # TODO: uplaod small mario as the user's mouse
        self.image = pygame.transform.scale(self.image, (57,78))
        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()
        self.hp = 250
    def hp_remaining(self) -> int:
        return self.hp / 250


class Block(pygame.sprite.Sprite):
    """Describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
    """
    def __init__(self, colour: tuple, width: int, height: int) -> None:
        """
        Arguments:
        :param colour: 3-tuple (r, g, b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()
class Enemy(pygame.sprite.Sprite):
    """The enemy sprites
    Attribute:
        images: Surface that is the visual representation
        rect: Rect (x, y, width, height)"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/smb_goomba.png")
        # resize the image
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        # define the initial location
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )
        # Define the initial velocity
        self.x_vel = random.choice([-4, -3,3,4])
        self.y_vel = random.choice([-4, -3,3,4])

    def update(self)-> None:
        """Calculate movement"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        # Constrain movement
        # X-
        if self.rect.left < 0:
            self.rect.x = 0
            self.x_vel = - self.x_vel # bounce
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = - self.x_vel # bounce
        # Y -
        if self.rect.y <0:
            self.rect.y = 0
            self.y_vel = - self.y_vel
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = - self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    score = 0
    num_enemies = 5
    time_start = time.time()
    time_invincible = 2

    font = pygame.font.SysFont("Arial", 25)
    pygame.mouse.set_visible(False)

    # Create groups to hold Sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemey_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):
        # Create a block (set its parameters)
        block = Block(BLACK, 20, 15)

        # Set a random location for the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)

        # Add the block to the block_sprites Group
        # Add the block to the all_sprites Group
        block_sprites.add(block)
        all_sprites.add(block)

    # Craete enemy sprites
    for i in range(num_enemies):
        # Create an enemy
        enemy = Enemy()
        # Add it to the sprites list (enemy_sprites and all_sprites)
        enemey_sprites.add(enemy)
        all_sprites.add(enemy)
    # Create the Player block
    player = Player()
    # Add the Player to all_sprites group
    all_sprites.add(player)

    pygame.mouse.set_visible(True)


    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos

        mouse_pos = pygame.mouse.get_pos()
        player.rect.x, player.rect.y = mouse_pos[0]-player.rect.width/2, mouse_pos[1]-player.rect.height/2

        # make all sprites move
        all_sprites.update()
        enemies_collided = pygame.sprite.spritecollide(player, enemey_sprites, False)


        # Check all collisions between player and ENEMY


        # set a time for invincibility at the beginning of the game
        if time.time() - time_start > time_invincible:
            for enemy in enemies_collided:
                player.hp -= 10
            blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)
            for block in blocks_collided:
                score += 1
        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        # Draw all sprites
        all_sprites.draw(screen)

        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5,5)
        )

        pygame.draw.rect(screen, GREEN, [580, 5, 215, 20])
        # Draw the foreground rectangle which is the remaining health
        life_remaining = 215 - int(215 * player.hp_remaining())
        pygame.draw.rect(screen, BLUE, [580, 5, life_remaining, 20])

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()