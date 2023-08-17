from random import randint
import prompt
import operator

from brain_games.common_functions import knockout_user, welcome_user

OPERATORS = ['+', '-', '*']


def choice_operator(first_number, second_number, select_operator):
    operators = {
        '+': operator.add(first_number, second_number),
        '-': operator.sub(first_number, second_number),
        '*': operator.mul(first_number, second_number)
    }

    return operators.get(select_operator)


def brain_calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        first_random_number = randint(0, 100)
        second_random_number = randint(0, 100)
        random_symbol = OPERATORS[randint(0, 2)]
        print(f'Question: '
              f'{first_random_number} {random_symbol} {second_random_number}')
        answer = prompt.integer('Your answer: ')
        correct_answer = choice_operator(first_random_number,
                                         second_random_number, random_symbol)
        if answer != correct_answer:
            knockout_user(answer, correct_answer, name)
            return None
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')
    return None
