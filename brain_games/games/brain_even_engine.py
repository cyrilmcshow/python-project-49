from random import randint
import prompt

from brain_games.common_functions import knockout_user, welcome_user


def even_or_not(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def brain_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ').lower()
        correct_answer = even_or_not(random_number)
        if answer != correct_answer:
            knockout_user(answer, correct_answer, name)
            return None
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
    return None
