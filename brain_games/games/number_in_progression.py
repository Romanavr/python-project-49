from random import randrange

GAME_DESCRIPTION = 'What number is missing in the progression?'


def game_handler():
    start = randrange(1, 101)
    step = randrange(1, 11)
    progression = list(range(start, start + 100, step))[:10]
    random_num = randrange(1, 10)
    answer = progression[random_num]
    progression[random_num] = '..'
    progression = ' '.join(str(x) for x in progression)

    return progression, answer
