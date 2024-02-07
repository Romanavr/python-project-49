import prompt
from brain_games import cli

MAX_ATTEMPTS = 3


def start_game(game_description, game_handler):
    user_name = cli.welcome_user()
    print(game_description)
    result = play_game(game_handler)
    if result:
        print(f'Congratulations, {user_name}!')
    else:
        print(f'Let\'s try again, {user_name}!')


def ask_question(expression):
    print(f'Question: {expression}')
    return prompt.string('Your answer: ').lower().strip()


def play_game(game_handler):
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        question, answer = game_handler()
        user_answer = ask_question(question)
        if str(answer) != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            return False
        print('Correct!')
        attempts += 1
    return True
