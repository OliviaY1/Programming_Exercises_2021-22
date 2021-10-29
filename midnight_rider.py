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
        self.agents_distance = -28
        self.fuel = MAX_FUEL

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
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes
        the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()

        # Based on their choice, change the attributes
        # of the class
        if user_choice == "q":
            self.done = True
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

def main() -> None:
    game = Game() # starting a new game
    game.introduction()

    # Main Loop
    while not game.done:
        # Display the choices to the player
        game.show_choices()
        # Ask the player what they want to do
        game.get_choice()
        # TODO: Change the state of the environment
        # TODO: Check win/lose conditions

if __name__ == "__main__":
    main()