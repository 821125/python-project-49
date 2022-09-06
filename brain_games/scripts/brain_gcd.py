#!/usr/bin/env pyhton3
from brain_games.cli import greeting, welcome_user
from random import randint
from math import gcd


def main():

    greeting()
    name = welcome_user()

    print('Find the greatest common divisor of given numbers.')

    count = 0
    while count < 3:
        num1, num2 = randint(1, 99), randint(1, 99)
        print(f'Question: {num1} {num2}')
        ans = int(input('Your answer: '))
        tr_ans = gcd(num1, num2)
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
