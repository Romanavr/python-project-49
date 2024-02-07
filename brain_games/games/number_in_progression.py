from random import randrange
from brain_games.games.game_engine import start_game

GAME_DESCRIPTION = 'What number is missing in the progression?'


def game_handler():
    start = randrange(1, 101)
    step = randrange(1, 11)
    progression = list(range(start, start + 100, step))[:10]
    random_num = randrange(1, 10)
    answer = progression[random_num]
    progression[random_num] = '..'

    return progression, answer


def new_game():
    start_game(GAME_DESCRIPTION, game_handler)
