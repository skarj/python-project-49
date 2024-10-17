from random import randint
from math import sqrt

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def get_question_and_answer():
    number = randint(1, 100)
    answer = 'yes' if is_number_prime(number) else 'no'

    return number, answer
