from random import randint

START_MESSAGE = 'Find the greatest common divisor of given numbers.'


def get_gcd(a, b):
    '''
    Finds the Greatest Common Divisor using Euclid's algorithm
    '''
    while b:
        a, b = b, a % b

    return a


def get_question_and_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    question = f'{number1} {number2}'
    answer = str(get_gcd(number1, number2))

    return question, answer
