from random import randrange
from math import gcd


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game_handler():
    num_1 = randrange(100)
    num_2 = randrange(100)
    question = f'{num_1} {num_2}'
    answer = gcd(num_1, num_2)

    return question, answer
