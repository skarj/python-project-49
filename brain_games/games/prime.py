from random import randint
from math import sqrt


def is_number_prime(number):
    prime_flag = 0

    if number > 1:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return False


def get_question_and_answer():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    number = randint(1, 100)
    answer = 'yes' if is_number_prime(number) else 'no'

    return number, answer
