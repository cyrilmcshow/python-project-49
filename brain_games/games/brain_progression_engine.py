from random import randint
import prompt

from brain_games.common_functions import knockout_user, welcome_user


def brain_progression_game():
    name = welcome_user()

    print('What number is missing in the progression?')

    for _ in range(3):
        left_borders = randint(10, 16)
        right_borders = randint(80, 96)
        step = randint(5, 10)
        progression = [x for x in range(left_borders, right_borders, step)]
        progression.sort()
        random_number = progression[randint(0, 7)]
        index = progression.index(random_number)
        progression[index] = '..'
        result_for_print = " ".join(map(str, progression))
        print(f'Question: {result_for_print}')
        answer = prompt.integer('Your answer: ')
        if answer != random_number:
            knockout_user(answer, random_number, name)
            return None
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')

    return None
