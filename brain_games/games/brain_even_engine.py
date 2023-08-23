from random import randint
import prompt

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_or_not(number):
    if number % 2 == 0:
        return True
    else:
        return


def play_brain_even():
    random_number = randint(0, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ').lower()
    if even_or_not(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return answer, correct_answer
