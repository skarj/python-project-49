from brain_games.engine.game import start_game
from random import randint


def get_question():
    step = randint(1, 5)
    start = randint(1, 15)
    index = randint(0, 9)

    sequence = [str(i) for i in range(start, start + step * 10, step)]
    answer = sequence[index]
    sequence[index] = '..'
    question = ' '.join(sequence)

    return question, answer


def play():
    title = "What number is missing in the progression?"
    start_game(get_question, title)
