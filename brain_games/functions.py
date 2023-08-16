from random import randint
import prompt

symbols = ['+', '-', '*']


def even_or_not(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def knockout_user(answer, correct_answer, name):
    print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}". ')
    print(f"Let's try again, {name}")


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


def brain_calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        first_random_number = randint(0, 100)
        second_random_number = randint(0, 100)
        random_symbol = symbols[randint(0, 2)]
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
