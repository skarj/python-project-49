import prompt

GAME_ROUNDS_COUNT = 3


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


def start_game(get_question_and_answer):
    '''
    Main game function
    '''
    player_name = greet()

    for _ in range(GAME_ROUNDS_COUNT):
        question_text, correct_answer = get_question_and_answer()
        player_answer = ask_question(question_text)

        if str(player_answer) == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {player_name}!")
            return

    print(f'Congratulations, {player_name}!')
