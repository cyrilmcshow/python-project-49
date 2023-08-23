#!/usr/bin/env python3

from brain_games.games.brain_even_engine import play_brain_even, TASK
from brain_games.engine import games_engine


def main():
    games_engine(TASK, play_brain_even)


if __name__ == '__main__':
    main()
