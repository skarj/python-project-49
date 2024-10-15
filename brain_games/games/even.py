from random import randint


def get_question_and_answer():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    number = randint(1, 100)
    answer = 'yes' if number % 2 == 0 else 'no'

    return number, answer
