#!/usr/bin/env pyhton3
from brain_games.cli import greeting, welcome_user
from random import randint, choice


def main():

    greeting()
    name = welcome_user()

    print('What is the result of the expression?')

    count = 0
    while count < 3:
        sign = choice('+-*')
        expression = f'{randint(1, 99)} {sign} {randint(1, 99)}'
        print(f'Question: {expression}')
        answer = int(input('Your answer: '))
        true_answer = int(eval(expression))
        if answer == true_answer:
            print("Correct!")
            count += 1
        else:
            print(f"{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print(f"Let's try, again, {name}!")

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
