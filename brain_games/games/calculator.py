from random import randrange

GAME_DESCRIPTION = 'What is the result of the expression?'


def game_handler():
    operator = ['+', '-', '*'][randrange(0, 3)]
    operand_a = randrange(100)
    operand_b = randrange(100)
    question = f'{operand_a} {operator} {operand_b}'
    answer = eval(question)

    return question, answer
