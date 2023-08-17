from random import randint
from math import gcd
import prompt

from brain_games.common_functions import knockout_user, welcome_user


def brain_gcd_game():
    name = welcome_user()

    print('Find the greatest common divisor of given numbers.')

    for _ in range(3):
        first_random_number = randint(0, 100)
        second_random_number = randint(0, 100)
        print(f'Question: {first_random_number} {second_random_number}')
        answer = prompt.integer('Your answer: ')
        correct_answer = gcd(first_random_number, second_random_number)
        if answer != correct_answer:
            knockout_user(answer, correct_answer, name)
            return None
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')
    return None
