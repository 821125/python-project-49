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
        answer = int(input('Your answer: '))
        true_answer = gcd(num1, num2)
        if answer == true_answer:
            print("Correct!")
            count += 1
        else:
            print(f"{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print(f"Let's try, again, {name}!")

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
