#!/usr/bin/env python3

from ..engine.game import game
from random import randint
from math import gcd


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
    task = "Find the greatest common divisor of given numbers."
    game(get_question, task)


if __name__ == '__main__':
    main()
