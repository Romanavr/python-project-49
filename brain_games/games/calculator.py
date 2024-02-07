from random import randrange
from brain_games.games.game_engine import start_game

GAME_DESCRIPTION = 'What is the result of the expression?'


def game_handler():
    operator = ['+', '-', '*'][randrange(0, 3)]
    operand_a = randrange(100)
    operand_b = randrange(100)
    question = f'{operand_a} {operator} {operand_b}'
    answer = eval(question)

    return question, answer


def new_game():
    start_game(GAME_DESCRIPTION, game_handler)
