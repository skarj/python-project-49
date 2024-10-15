from random import randint


def get_question_and_answer():
    number = randint(1, 100)
    answer = 'yes' if number % 2 == 0 else 'no'

    return number, answer
