#!/usr/bin/env python3

from brain_games.engine import start_game
from brain_games.games.progression import get_question_and_answer


def main():
    print("What number is missing in the progression?")
    start_game(get_question_and_answer)


if __name__ == '__main__':
    main()
