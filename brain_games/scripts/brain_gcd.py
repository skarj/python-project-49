#!/usr/bin/env python3

from brain_games.engine import start_game
from brain_games.games.gcd import get_question_and_answer


def main():
    print('Find the greatest common divisor of given numbers.')
    start_game(get_question_and_answer)


if __name__ == '__main__':
    main()
