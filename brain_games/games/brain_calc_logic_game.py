from random import randint
import prompt
import operator

TASK = 'What is the result of the expression?'

OPERATORS = ['+', '-', '*']


def choice_operator(first_number, second_number, select_operator):
    operators = {
        '+': operator.add(first_number, second_number),
        '-': operator.sub(first_number, second_number),
        '*': operator.mul(first_number, second_number)
    }

    return operators.get(select_operator)


def play_brain_calc():
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    random_symbol = OPERATORS[randint(0, 2)]
    print(f'Question: '
          f'{first_random_number} {random_symbol} {second_random_number}')
    answer = prompt.integer('Your answer: ')
    correct_answer = choice_operator(first_random_number,
                                     second_random_number, random_symbol)
    return answer, correct_answer
