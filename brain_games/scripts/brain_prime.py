#!/usr/bin/env python3

from brain_games.games.brain_prime_logic_game import play_brain_prime, TASK
from brain_games.engine import games_engine


def main():
    games_engine(TASK, play_brain_prime)


if __name__ == '__main__':
    main()
