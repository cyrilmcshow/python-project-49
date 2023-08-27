from random import randint
import prompt

task = 'What number is missing in the progression?'


def generate_number_from_progression(lower_bound, upper_bound, step):
    progression = [x for x in range(lower_bound, upper_bound, step)]
    random_number = progression[randint(0, 6)]
    index = progression.index(random_number)
    progression[index] = '..'
    result_for_print = " ".join(map(str, progression))
    return result_for_print, random_number


def play_brain_progression():
    lower_bound = randint(10, 16)
    upper_bound = randint(80, 96)
    step = randint(5, 10)
    result_for_print, random_number = generate_number_from_progression(
        lower_bound, upper_bound, step)
    print(f'Question: {result_for_print}')
    answer = prompt.integer('Your answer: ')
    return answer, random_number
