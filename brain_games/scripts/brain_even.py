#!/usr/bin/env python3

from brain_games.games.brain_even import play_brain_even, task
from brain_games.engine import launch_games_engine


def main():
    launch_games_engine(task, play_brain_even)


if __name__ == '__main__':
    main()
