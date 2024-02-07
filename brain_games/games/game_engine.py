import prompt
from brain_games import cli
from brain_games.games import even_number
from brain_games.games import calculator
from brain_games.games import gcd_number
from brain_games.games import number_in_progression
from brain_games.games import prime_number

MAX_ATTEMPTS = 3


def start_game(game_description: str, game_handler: callable) -> str:
    user_name = cli.welcome_user()
    print(game_description)
    result = play_game(game_handler)
    if result:
        print(f'Congratulations, {user_name}!')
    else:
        print(f'Let\'s try again, {user_name}!')


def ask_question(question: str) -> str:
    print(f'Question: {question}')
    return prompt.string('Your answer: ').lower().strip()


def play_game(game_handler: callable) -> bool:
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        question, answer = game_handler()
        user_answer = ask_question(question)
        if str(answer) != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")  # noqa: E501
            return False
        print('Correct!')
        attempts += 1
    return True


def new_game(game_name: str) -> callable:
    game_library = {
        'even': even_number,
        'calc': calculator,
        'gcd': gcd_number,
        'progression': number_in_progression,
        'prime': prime_number,
    }
    selected_game = game_library[game_name]
    start_game(selected_game.GAME_DESCRIPTION, selected_game.game_handler)
