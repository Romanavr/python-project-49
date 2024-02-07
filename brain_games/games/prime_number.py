from random import randrange
from brain_games.games.game_engine import start_game

GAME_DESCRIPTION = f'Answer "yes" if given number is prime.Otherwise answer "no".'


def is_number_prime(number):
    if number <= 1 or number % 2 == 0:
        return number, 'no'
    for i in range(3, number, 2):
        print(i)
        if number % i == 0:
            return number, 'no'
    return number, 'yes'


def game_handler():
    number = randrange(1, 101)
    return number, 'yes' if is_number_prime(number) else 'no'


def new_game():
    start_game(GAME_DESCRIPTION, game_handler)
