from brain_games.engine.game import start_game
from random import randint, choice
from operator import add, sub, mul


def get_question():
    number1 = randint(1, 50)
    number2 = randint(1, 50)

    operation_action = {
        '+': add,
        '-': sub,
        '*': mul,
    }

    operation, action = choice(list(operation_action.items()))
    question = f'{number1} {operation} {number2}'
    answer = action(number1, number2)

    return question, answer


def play():
    title = 'What is the result of the expression?'
    start_game(get_question, title)
