import prompt

ATTEMPTS = 3


def greet():
    '''
    Asks user for the name and says hello
    '''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    return name


def ask_question(question):
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


def start_game(get_question, title):
    '''
    Main game function
    '''
    player_name = greet()
    print(title)

    game_failed = False
    for _ in range(ATTEMPTS):
        qestion_text, correct_answer = get_question()
        player_answer = ask_question(qestion_text)

        if str(player_answer) == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {player_name}!")
            failed = True
            return

    if not game_failed:
        print(f'Congratulations, {player_name}!')
