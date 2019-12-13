import random
import collections

class CheatingError:
    pass

class Game:
    def __init__(self, print_func=print, input_func=input):
        """initiates new instance of the game"""
        self._print = print_func
        self._input = input_func

    def begin(self, num_rounds=10):
        """begins the game by welcoming user, prompting them to begin"""
        print('Welcome to Game of Greed')
        answer = input('Wanna play? ')

        if answer == 'y':
            self.each_turn()
        else:
            print('OK. Maybe another time.')

    def dice_roll(self, num_dice):
        """creates instance of 6 dice being rolled"""
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
        num_dice = 6

        score = 0

        while(True):
            self._print(f'Rolling {num_dice} dice')

            roll = self.dice_roll(num_dice)
            check_score = self.calculate_score(roll)

            if check_score == 0:
                self._print('Well, shoot. No points this time')
                return 0

            keepers = self.validate_roll(roll)

            #TODO: handle non-scoring, but saved dice
            num_dice -= len(keepers)

            score += self.calculate_score(keepers)

            self._print(f'You can bank {score} points or try for more')

            if num_dice == 0:
                num_dice = 6

            self._print(f'You have {num_dice} left')

            roll_again_response = self._input('Roll again? ')

            if not roll_again_response == 'y':
                break

        return score

    def validate_roll(self, roll):
        """Handles roll of dice and numbers returned/dice kept"""
        while True:
            self._print(roll)

            keep_response = self._input('Which would you like to keep?')

            keepers = tuple(int(char) for char in keep_response)

            if self.validate(roll, keepers):
                return keepers
            else:
                self._print('Invalid answer')
                self._print(roll)

    def validate(self, roll, keepers):
        """handles count of dice"""
        roll_counter = Counter(roll)

        keepers_counter = Counter(keepers)

        return len(keepers_counter - roll_counter) == 0

    def play(self):
        """Handles score per turn of player"""
        self.score = 0
        round_num = 1

        for i in range(1, self.num_rounds + 1):
            round_score = self.each_turn()

            self._print(f'You banked {round_score} points in round {round_num}')

            self.score += round_score

            round_num += 1

            self._print(f'You have {self.score} points total')

        self._print('Thanks for playing!')

if __name__ == "__main__":
    game = Game()

    game.begin()
