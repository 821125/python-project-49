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