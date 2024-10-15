from random import randint, choice
from operator import add, sub, mul


def get_question_and_answer():
    number1 = randint(1, 50)
    number2 = randint(1, 50)

    operation_action = {
        '+': add,
        '-': sub,
        '*': mul,
    }

    operation, action = choice(list(operation_action.items()))
    question = f'{number1} {operation} {number2}'
    answer = str(action(number1, number2))

    return question, answer
