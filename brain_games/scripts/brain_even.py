import prompt
from brain_games import cli
from random import randrange


def ask_number():
    random_number = randrange(100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    expected_anmswer = 'yes' if random_number % 2 == 0 else 'no'
    if answer.lower() == expected_anmswer:
        return True, answer, expected_anmswer
    return False, answer, expected_anmswer


def even_number_game():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attemps = 0
    while attemps < 3:
        result, ans, ans_e = ask_number()
        if not result:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{ans_e}'.")
            print(f'Let\'s try again, {name}')
            return False
        print('Correct!')
        attemps += 1
    print(f'Congratulations, {name}!')


def main():
    even_number_game()


if __name__ == '__main__':
    main()
