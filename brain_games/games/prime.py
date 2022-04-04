from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def get_puzzle():
  num = randint(2, 50)
  answer = 'yes' if is_prime(num) else 'no'
  return (num, answer)
