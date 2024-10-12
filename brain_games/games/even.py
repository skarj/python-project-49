from ..engine.game import start_game
from random import randint


def get_question():
    number = randint(1, 100)

    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return number, answer


def play():
    title = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(get_question, title)
