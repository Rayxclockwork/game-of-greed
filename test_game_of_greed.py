# import random
import pytest
from game_of_greed import Game


def test_game_instance():
    game = Game()
    assert game


# def test_greeting():
#     prints = ["Welcome to Game of Greed"]
#     prompts = ['Wanna play? ']
#     responses = ['y']

#     def testing_print(*args):
#         if len(prints):
#             current_print = prints.pop(0)
#             assert args[0] == current_print

#     def testing_input(*args):
#         if len(prompts):
#             current_prompt = prompts.pop(0)
#             assert args[0] == current_prompt

#         if len(responses):
#             current_response = responses.pop(0)
#             return current_response

#     game = Game(testing_print, testing_input)
#     game.play()


def test_calculate_score(game, dice, expected):
    actual = game.calculate_score(dice)
    assert actual == expected


def test_calc_score_simple():
    g = Game()
    actual = g.calculate_score((1, 2))
    expected = 100
    assert expected == actual


def test_zilch(game):
    expected = 0
    actual = game.calculate_score((2, 3, 4, 6, 2, 3))
    assert actual == expected


def test_ones(game):
    expected = 4000
    actual = game.calculate_score((1, 1, 1, 1, 1, 1))
    assert actual == expected


def test_twos(game):
    expected = 400
    actual = game.calculate_score((4, 2, 2, 6, 2, 2))
    assert actual == expected


def test_threes(game):
    expected = 300
    actual = game.calculate_score((6, 3, 2, 3, 3, 4))
    assert actual == expected


def test_fours(game):
    expected = 1600
    actual = game.calculate_score((4, 4, 4, 4, 4, 4))
    assert actual == expected


def test_fives(game):
    expected = 1000
    actual = game.calculate_score((5, 6, 4, 5, 5, 5))
    assert actual == expected


def test_sixes(game):
    expected = 600
    actual = game.calculate_score((2, 6, 3, 6, 6, 4))
    assert actual == expected


def test_straight(game):
    expected = 1500
    actual = game.calculate_score((6, 3, 4, 2, 1, 5))
    assert expected == actual


def test_mcflurry(game):
    expected = 2000
    actual = game.calculate_score((5, 1, 5, 5, 6, 5))
    assert expected == actual


def test_three_pairs(game):
    expected = 1500
    actual = game.calculate_score((5, 4, 1, 5, 1, 4))
    assert expected == actual


# @pytest.mark.skip('pending')
# def test_two_trios(game):
#     expected =
#     actual = game.calculate_score(())
#     assert actual == expected


# @pytest.mark.skip('pending')
# def test_leftover_ones(game):
#     expected =
#     actual = game.calculate_score(())
#     assert actual == expected


# @pytest.mark.skip('pending')
# def test_leftover_fives(game):
#     expected =
#     actual = game.calculate_score(())
#     assert actual == expected


@pytest.fixture()
def game():
    return Game()
