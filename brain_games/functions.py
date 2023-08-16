from random import randint
import prompt


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


def brain_even_game():
    name = welcome_user()
    for _ in range(3):
        print('Answer "yes" if the number is even, otherwise answer "no".')
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ').lower()
        if answer != even_or_not(random_number):
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{even_or_not(random_number)}". ')
            print(f"Let's try again, {name}")
            return None
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
    return None
