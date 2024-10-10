#!/usr/bin/env python3

from ..engine.game import game
from random import randint


def is_number_prime(number: int):
    if number == 1:
        return False

    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1

    return True


def get_question():
    number = randint(1, 100)

    if is_number_prime(number):
        answer = "yes"
    else:
        answer = "no"

    return number, answer


def main():
    title = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game(get_question, title)


if __name__ == '__main__':
    main()
