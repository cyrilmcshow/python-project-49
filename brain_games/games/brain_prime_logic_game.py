from random import randint
import prompt

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        return True
    else:
        return


def play_brain_prime():
    random_number = randint(0, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ').lower()
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return answer, correct_answer
