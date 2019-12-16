from game_of_greed import Game

class BotPlayer:
    def __init__(self):
        self.roll = None

    def _print(self, *args):
        print('bot')
        print(args[0])

    def _input(self, *args):
        print(args[0], 'n')
        return 'n'

class ParticipationTrophy:

    def _print(self, *args):
        print (args[0])

        msg = args[0]

        if msg.startswith('You rolled '):
            self.roll = [int(char) for char in msg if char.isdigit()]

        print(msg)

    def _input(self, *args):
        prompt = args[0]

        if prompt == 'Wanna play? ':
            print(prompt, 'y')
            return 'y'

        if prompt == 'which would you like to keep? ':

            score = self.game.calculate_score(self.roll)
            #figure this out

            if 1 in self.roll:
                return '1'
            if 5 in self.roll:
                return '5'


if __name__ == "__main__":
    bot = ParticipationTrophy()
    game = Game(bot._print, bot._input)
    game.begin()
