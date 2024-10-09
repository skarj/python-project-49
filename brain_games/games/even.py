#!/usr/bin/env python3

from ..engine.game import game
from random import randint


def get_question():
    number = randint(1, 100)

    if number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"

    return number, answer


def main():
    ques_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    game(get_question, ques_message)


if __name__ == '__main__':
    main()
