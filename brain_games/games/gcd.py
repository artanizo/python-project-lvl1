from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_puzzle():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    answer = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return (question, str(answer))
