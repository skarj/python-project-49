from brain_games.engine.game import start_game
from random import randint


def get_question():
    number = randint(1, 100)
    answer = 'yes' if number % 2 == 0 else "no"

    return number, answer


def play():
    title = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(get_question, title)
