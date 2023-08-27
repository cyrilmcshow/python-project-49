#!/usr/bin/env python3

from brain_games.games.brain_prime import play_brain_prime, task
from brain_games.engine import launch_games_engine


def main():
    launch_games_engine(task, play_brain_prime)


if __name__ == '__main__':
    main()
