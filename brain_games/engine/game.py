import prompt
from sys import exit


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    return name


def ask_question(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')

    return answer


def is_answer_correct(answer, correct):
    if str(answer) == str(correct):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        return False


def game(question, title):
    name = greeting()
    print(title)

    attempt = 0
    while attempt < 3:
        qes_text, qes_result = question()
        answer = ask_question(qes_text)
        if not is_answer_correct(answer, qes_result):
            print(f"Let's try again, {name}!")
            exit(1)
        attempt += 1

    print(f"Congratulations, {name}!")
