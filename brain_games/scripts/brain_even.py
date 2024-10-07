#!/usr/bin/env python3

from ..cli import say_hello
from random import randint
import prompt


def check_answer(answer, correct):
    if answer == correct:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        return False


def main():
    name = say_hello()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    attempt = 0
    while attempt < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')

        if random_number % 2 == 0:
            result = check_answer(answer, "yes")
            if not result:
                break
        else:
            result = check_answer(answer, "no")
            if not result:
                break

        attempt += 1

    if not result:
        print(f"Let's try again, {name}!")
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
