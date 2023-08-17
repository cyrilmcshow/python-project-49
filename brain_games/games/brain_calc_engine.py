from random import randint
import prompt

from brain_games.common_functions import knockout_user, welcome_user

SYMBOLS = ['+', '-', '*']


def brain_calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        first_random_number = randint(0, 100)
        second_random_number = randint(0, 100)
        random_symbol = SYMBOLS[randint(0, 2)]
        print(f'Question: {first_random_number} {random_symbol} {second_random_number}')
        answer = prompt.integer('Your answer: ')

        if random_symbol == '+':
            correct_answer = first_random_number + second_random_number
            if answer != correct_answer:
                knockout_user(answer, correct_answer, name)
                return None
            else:
                print('Correct!')

        if random_symbol == '-':
            correct_answer = first_random_number - second_random_number
            if answer != correct_answer:
                knockout_user(answer, correct_answer, name)
                return None
            else:
                print('Correct!')

        if random_symbol == '*':
            correct_answer = first_random_number * second_random_number
            if answer != correct_answer:
                knockout_user(answer, correct_answer, name)
                return None
            else:
                print('Correct!')

    print(f'Congratulations, {name}!')
    return None
