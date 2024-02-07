from random import randrange

GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


def is_number_prime(number):
    if number <= 1 or number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


def game_handler():
    number = randrange(1, 101)
    return number, ('yes' if is_number_prime(number) else 'no')
