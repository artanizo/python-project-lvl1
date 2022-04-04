from random import randint

description = 'What number is missing in the progression?'

progression_len = 10


def get_puzzle():
    hidden_index = randint(0, progression_len - 1)
    current = randint(0, 100)
    step = randint(1, 10)
    question = str(current)
    answer = 0
    for x in range(progression_len):
        current = current + step
        if x == hidden_index:
            answer = current
            question += ' ..'
        else:
            question += f' {current}'
    return (question, str(answer))
