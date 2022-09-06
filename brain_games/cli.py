from prompt import string
from random import randint


def greeting():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_progression():
    start = randint(1, 9)
    step = randint(2, 4)
    finish = start + 10 * step
    progression = list(range(start, finish, step))
    return list(map(str, progression))


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
