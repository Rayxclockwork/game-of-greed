# import random
import collections


class Game:
    def __init__(self, print_func=print, input_func=input):
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

    def calculate_score(self, dice):
        """randomizes 6 dice rolls"""
        score = 0
        pairs = 0
        count = collections.Counter(dice)

        """Grand Mcflurry"""
        if count[5] == 4 and count[1] == 1:
            score += 2000
            return score

        """Straights"""
        if 1 in count and 2 in count and 3 in count and 4 in count and 5 in count and 6 in count:
            score += 1500
            return score

        """Pairs"""
        for i in count:
            if count[i] == 2:
                pairs += 1
                if pairs == 3:
                    score = 0
                    score += 1500
                    return score

        """Less than 3 fives"""
        if count[i] < 3 and i == 5:
            score += (count[i] * 50)

        """Less than 3 ones"""
        if count[i] < 3 and i == 1:
            score += (count[i] * 100)

        """Three ones and any extra ones"""
        if count[i] >= 3 and i == 1:
            score += 1000
            count[i] -= 3
            for i in range(count[i]):
                score += 1000

        """Three of a kind for anything other than ones"""
        if count[i] >= 3 and i != 1:
            score += (i * 100)
            count[i] -= 3
            for i in range(count[i]):
                score += 100

        return score


if __name__ == "__main__":
    game = Game()

    game.play()
