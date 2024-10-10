#!/usr/bin/env python3

from ..engine.game import game
from random import randint, choice


def get_question():
    number1 = randint(1, 50)
    number2 = randint(1, 10)
    action = choice(['+', '-', '*'])

    question = f"{number1} {action} {number2}"
    if action == "+":
        answer = number1 + number2
    elif action == "-":
        answer = number1 - number2
    else:
        answer = number1 * number2

    return question, answer


def main():
    title = 'What is the result of the expression?'
    game(get_question, title)


if __name__ == '__main__':
    main()
