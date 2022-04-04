from random import randint, choice

description = 'What is the result of the expression?'

operators = '+-*'


def calc(operator, a, b):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b


def get_puzzle():
    first_operand = randint(0, 50)
    second_operand = randint(0, 50)
    operator = choice(operators)
    answer = calc(operator=operator, a=first_operand, b=second_operand)
    question = f'{first_operand} {operator} {second_operand}'
    return (question, str(answer))
