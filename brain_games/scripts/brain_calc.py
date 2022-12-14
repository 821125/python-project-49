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
        ans = int(input('Your answer: '))
        tr_ans = int(eval(expression))
        if ans == tr_ans:
            print("Correct!")
            count += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{tr_ans}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
