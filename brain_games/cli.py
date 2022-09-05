from prompt import string


def greeting():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
