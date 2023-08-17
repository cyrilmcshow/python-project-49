from random import randint
import prompt

from brain_games.common_functions import knockout_user, welcome_user


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        return 'yes'
    else:
        return 'no'


def brain_prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ').lower()
        correct_answer = is_prime(random_number)
        if correct_answer != answer:
            knockout_user(answer, correct_answer, name)
            return None
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')

    return None
