from random import randint


def get_question_and_answer():
    step = randint(1, 5)
    start = randint(1, 15)
    index = randint(0, 9)

    sequence = [str(i) for i in range(start, start + step * 10, step)]
    answer = str(sequence[index])
    sequence[index] = '..'
    question = ' '.join(sequence)

    return question, answer
