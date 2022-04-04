import prompt


ROUNDS = 3


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def run_game(description, get_puzzle):
    name = greet()
    print(description)
    for x in range(ROUNDS):
        (question, answer) = get_puzzle()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if (answer != user_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            print(f"Let\'s try again, {name}!")
            break
        else:
            print('Correct!')
    if (x == (ROUNDS - 1)):
        print(f'Congratulations, {name}!')
