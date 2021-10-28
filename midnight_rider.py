# Midnight Rider

# A text-based game of intrigue and illusion
import midnight_rider_text


# Create a class called "Game", where it has a function called ""introduction
class Game:
    '''Represent our game engine
    '''
    def introduction(self) -> None:
        """Print the introduction text"""
        # TODO: print the introduction text
        print(midnight_rider_text.INTRODUCTION)

def main() -> None:
    game = Game() # starting a new game
    game.introduction()

if __name__ == "__main__":
    main()