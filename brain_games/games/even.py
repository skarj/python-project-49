from random import randint


def game():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    number = randint(1, 100)
    answer = 'yes' if number % 2 == 0 else "no"

    return number, answer
