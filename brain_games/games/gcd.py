from brain_games.engine.game import start_game
from random import randint


def get_gcd(a, b):
    '''
    Finds the Greatest Common Divisor using Euclid's algorithm
    '''
    while b:
        a, b = b, a % b

    return a


def get_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    question = f'{number1} {number2}'
    answer = get_gcd(number1, number2)

    return question, answer


def play():
    title = 'Find the greatest common divisor of given numbers.'
    start_game(get_question, title)
