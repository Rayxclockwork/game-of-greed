import random
import collections

class Game:
    def __init__(self, print_func=print, input_func=input):
        """initiates new instance of the game"""
        self._print = print_func
        self._input = input_func

    def begin(self):
        """begins the game by welcoming user, prompting them to begin"""
        print('Welcome to Game of Greed')
        answer = input('Wanna play? ')

        if answer == 'y':
            print('Great! Check back tomorrow. :D')
        else:
            print('OK. Maybe another time.')

    def dice_roll(self, num_dice):
        num_dice = 6
        return tuple(random.randint(1, 6) for i in range(num_dice))

    def calculate_score(self, dice):
        """randomizes 6 dice rolls"""
        score = 0
        pairs = 0
        count = collections.Counter(dice)

        """Grand Mcflurry"""
        if count[5] == 4 and count[1] == 1:
            score += 2000
            return 2000

        """Straights"""
        if 1 in count and 2 in count and 3 in count and 4 in count and 5 in count and 6 in count:
            score += 1500
            return 1500

        """Pairs"""
        for i in count:
            if count[i] == 2:
                pairs += 1
                if pairs == 3:
                    return 1500

            """Less than 3 fives"""
            if count[i] < 3 and i == 5:
                score += (count[i] * 50)
                continue

            """Less than 3 ones"""
            if count[i] < 3 and i == 1:
                score += (count[i] * 100)

            """handles 3 or more of anything other than 1s"""
            if count[i] >= 3 and i != 1:
                score += ((count[i] - 2)*(i * 100))

            """handles 3 or more 1s"""
            if count[i] >= 3 and i == 1:
                score += ((count[i] -2)*(i * 1000))

        return score

    def each_turn(self):
        """handles each turn"""
        score = 0
        while score == 0:
            dice_roll()
            calculate_score()
            if score == 0:
                break
            else:
                print('You got ' + score + ' points')
                print('Would you like to bank points or roll again')
                if input('bank'):
                    dice_roll()
                else:
                    return score
                break
        #roll dice, calc score, prompt for save dice or bank points
        # if zilch, new turn

if __name__ == "__main__":
    game = Game()

    game.begin()
