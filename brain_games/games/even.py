from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_puzzle():
    num = randint(0, 100)
    is_num_even = is_even(num)
    answer = 'yes' if is_num_even else 'no'
    return (num, answer)
