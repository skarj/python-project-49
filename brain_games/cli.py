import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    return name


def ask_question(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')

    return answer
