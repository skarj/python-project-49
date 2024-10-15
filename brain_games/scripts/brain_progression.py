#!/usr/bin/env python3

from brain_games.engine.game import start_game
from brain_games.games.progression import get_question_and_answer


def main():
    start_game(get_question_and_answer)


if __name__ == '__main__':
    main()
