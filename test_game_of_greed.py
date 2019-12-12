# import random
import pytest
from game_of_greed import Game

def test_game_instance():
    game = Game()
    assert game

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

def test_calc_score_simple():
    game = Game()
    actual = game.calculate_score((1, 2))
    expected = 100
    assert expected == actual

def test_zilch(game):
    expected = 0
    actual = game.calculate_score((2, 3, 4, 6, 2, 3))
    assert actual == expected

def test_three_of_a_kind(game):
    expected = 400
    actual = game.calculate_score((4, 4, 4, 3, 2, 6))
    assert expected == actual

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

def test_two_trios(game):
    expected = 700
    actual = game.calculate_score((4, 3, 3, 4, 4, 3))
    assert actual == expected

def test_leftover_ones(game):
    expected = 200
    actual = game.calculate_score((3, 1, 6, 2, 1, 4))
    assert actual == expected

def test_leftover_fives(game):
    expected = 100
    actual = game.calculate_score((5, 6, 3, 2, 5, 3))
    assert actual == expected

@pytest.fixture()
def game():
    return Game()
