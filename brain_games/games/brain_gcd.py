from random import randint
from math import gcd
import prompt

task = 'Find the greatest common divisor of given numbers.'


def play_brain_gcd():
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    print(f'Question: {first_random_number} {second_random_number}')
    answer = prompt.integer('Your answer: ')
    correct_answer = gcd(first_random_number, second_random_number)
    return answer, correct_answer
