from random import randrange

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_handler():
    question = randrange(100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
