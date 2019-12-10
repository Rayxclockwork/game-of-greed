import random
import pytest
from game_of_greed import Game


def test_game_instance():
    game = Game()
    assert game


def test_greeting():
    prints = ["Welcome to Game of Greed"]
    prompts = ['Wanna play? ']
    responses = []

    def testing_print(message):
        if len(prints):
            assert message == prints.pop(0)

    def testing_input(prompt):
        if len(prompts):
            assert prompt == prompt.pop(0)

    game = Game(testing_print, testing_input)
    game.game()


# @pytest.mark.skip('pending')
# def test_zilch():
#     # # non scoring roll should return 0


# @pytest.mark.skip('pending')
# def test_ones():
#     # # rolls with various number of 1s should return correct score


# @pytest.mark.skip('pending')
# def test_twos():
#     # # rolls with various number of 2s should return correct score


# @pytest.mark.skip('pending')
# def test_threes():
#     # # rolls with various number of 3s should return correct score


# @pytest.mark.skip('pending')
# def test_fours():
#     # # rolls with various number of 4s should return correct score


# @pytest.mark.skip('pending')
# def test_fives():
#     # # rolls with various number of 5s should return correct score


# @pytest.mark.skip('pending')
# def test_sixes():
#     # # rolls with various number of 6s should return correct score


# @pytest.mark.skip('pending')
# def test_straight():
#     # # 1,2,3,4,5,6 should return correct score


# @pytest.mark.skip('pending')
# def test_three_pairs():
#     # # 3 pairs should return correct score


# @pytest.mark.skip('pending')
# def test_two_trios():
#     # # 2 sets of 3 should return correct score


# @pytest.mark.skip('pending')
# def test_leftover_ones():
#     # # 1s not used in set of 3 (or greater) should return correct score


# @pytest.mark.skip('pending')
# def test_leftover_fives():
#     # # 5s not used in set of 3 (or greater) should return correct score
