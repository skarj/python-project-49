from ..cli import greeting, ask_question
from sys import exit


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
