import random


class Game:
    def __init__(self, print_funct=print, input_func=input):
        """initiates new instance of the game"""
        self._print = print_func
        self._input = input_func


    def play(self):
        """begins the game by welcoming user, prompting them to begin"""
        print('Welcome to Game of Greed')
        answer = input('Wanna play? ')

        if answer == 'y':
            print('Great! Check back tomorrow. :D')
        else:
            print('OK. Maybe another time.')

    def calculate_score(self, dice_roll):
        """randomizes 6 dice rolls"""
        dice = ()

        d1 = random.randint(1, 6).append(dice)
        d2 = random.randint(1, 6).append(dice)
        d3 = random.randint(1, 6).append(dice)
        d4 = random.randint(1, 6).append(dice)
        d5 = random.randint(1, 6).append(dice)
        d6 = random.randint(1, 6).append(dice)



if __name__ == "__main__":
    game = Game()

    game.play()
