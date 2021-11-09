# Midnight Rider

# A text-based game of intrigue and illusion
import random

import midnight_rider_text
import sys
import textwrap
import time

MAX_FUEL = 50
MAX_TOFU = 3

# Create a class called "Game", where it has a function called ""introduction
class Game:
    '''Represent our game engine

        Attribute:
        done: describes if the game is
            finished or not - bool
        distance_traveled: describe the distance
            that we've traveled so far this game in km
        amount_of_tofu: how much tofu we have
            left in our inventory
        agents_distance: describes the distance
            between the player and the agents
    '''
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = 0

    def introduction(self) -> None:
        """Print the introduction text"""
        # TODO: print the introduction text
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect"""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush() # push the char out

    def show_choices(self) -> None:
        """Show user the choices"""
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes
        the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()

        # Based on their choice, change the attributes
        # of the class
        agents_distance_now = random.randrange(7,15)

        if user_choice == "q":
            self.done = True
        elif user_choice == 'a':
            # Consume one tofu IF and ONLY IF we have some
            # available
            # Decrease hunger to 0
            if self.amount_tofu > 0:
                self.amount_tofu -= 1
                self.hunger = 0
                # Give the player some feedback
                print(midnight_rider_text.EAT_TOFU)
            else:
                print(midnight_rider_text.NO_TOFU)

        elif user_choice == 'b':
            player_distance_now = random.randrange(5,10)
            self.distance_traveled += player_distance_now
            self.agents_distance += agents_distance_now - player_distance_now

            # Burn fuel
            self.fuel -= random.randrange(3, 8)

            # Give the player some feedback
            print(f"\n-------You drive conservatively.")
            print(f"-------You traveled {player_distance_now} kms.\n")

        elif user_choice == 'c':
            # Move the player
            player_distance_now = random.randrange(10,16)
            self.distance_traveled += player_distance_now
            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn fuel
            self.fuel -= random.randrange(5,11)
            # Give the player some feedback
            print(f"\n---------ZOOOOOOOOOOOOM")
            print(f"-------You traveled {player_distance_now} kms.\n")

        elif user_choice == "d":
            self.fuel = MAX_FUEL
            self.agents_distance += random.randrange(7,15)
            print(midnight_rider_text.REFUEL)

        elif user_choice == 'e':
            print(f"You have traveled {self.distance_traveled} km")
            print(f"Tofu pieces left: {self.amount_tofu}")
            print(f"Agent's Distance: {abs(self.agents_distance)} km behind")
            self.typewriter_effect("-----LOADING-----")
            time.sleep(2)
    def upkeep(self) -> None:
        """Give the uder reminders of hunger"""
        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)
        elif self.hunger > 25:
            print(midnight_rider_text.HUNGER)
        time.sleep(1)
    def check_endgame(self) ->None:
        if self.agents_distance >= 0:
            self.done = True
            self.endgame_reason = ENDGAME_REASONS["LOSE_AGENTS"]
        if self.fuel <= 0:
            self.done = True
            self.endgame_reason = ENDGAME_REASONS["LOSE_FUEL"]
        # LOSE - Perish because of hunger
        if self.hunger > MAX_HUNGER:
            self.done = True
            self.endgame_reason = ENDGAME_REASONS["LOSE_HUNGER"]
        if self.distance_traveled >= MAX_DISTSNCE:
            self.done = True
            self.endgame_reason = ENDGAME_REASONS["WIN"]


def main() -> None:
    game = Game() # starting a new game
    game.introduction()

    # Main Loop
    while not game.done:
        # Display the choices to the player
        game.upkeep()
        game.show_choices()
        # Ask the player what they want to do
        game.get_choice()
        game.check_endgame()
    time.sleep(2)
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )

if __name__ == "__main__":
    main()