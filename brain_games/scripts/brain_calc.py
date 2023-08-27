#!/usr/bin/env python3

from brain_games.games.brain_calc import play_brain_calc, task
from brain_games.engine import launch_games_engine


def main():
    launch_games_engine(task, play_brain_calc)


if __name__ == '__main__':
    main()
