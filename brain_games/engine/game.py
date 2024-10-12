import prompt
from sys import exit

ATTEMPTS = 3


def greet():
    '''
    Asks user for the name and says hello
    '''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    return name


def ask_question(question: str):
    '''
    Prints the question and asks for the answer
    '''
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')

    return answer


def is_answer_correct(answer, correct):
    '''
    Compares the user's answer with the correct answer
    and shows the result
    '''
    if str(answer) == str(correct):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        return False


def start_game(question, title: str):
    '''
    Main game function
    '''
    name = greet()
    print(title)

    for _ in range(ATTEMPTS):
        qestion_text, qestion_result = question()
        answer = ask_question(qestion_text)
        if not is_answer_correct(answer, qestion_result):
            print(f"Let's try again, {name}!")
            exit(0)

    print(f'Congratulations, {name}!')
