#!/usr/bin/env python3

from ..engine.game import game
from random import randint


def gcd(a, b):
    """
    Find GCD of two numbers using Eucliden algorithm
    """
    while b:
        a, b = b, a % b

    return a


def get_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    # Ensure numbers have a common divisor greater than 1
    while gcd(number1, number2) == 1:
        number1 = randint(1, 100)
        number2 = randint(1, 100)

    question = f"{number1} {number2}"
    answer = gcd(number1, number2)

    return question, answer


def main():
    ques_message = "Find the greatest common divisor of given numbers."
    game(get_question, ques_message)


if __name__ == '__main__':
    main()
