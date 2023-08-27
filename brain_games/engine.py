import prompt

NUMBER_OF_QUESTION = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def knockout_user(answer, correct_answer, name):
    print(f'"{answer}" is wrong answer ;(. '
          f'Correct answer was "{correct_answer}". ')
    print(f"Let's try again, {name}!")


def launch_games_engine(task, game_func):
    name = welcome_user()
    print(task)
    for _ in range(NUMBER_OF_QUESTION):
        answer, correct_answer = game_func()
        if answer != correct_answer:
            knockout_user(answer, correct_answer, name)
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
