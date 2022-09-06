#!/usr/bin/env pyhton3
from brain_games.cli import greeting, welcome_user, is_prime
from random import randint


def main():

    greeting()
    name = welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0
    while count < 3:
        number = randint(1, 99)
        print(f'Question: {number}')
        ans = input('Your answer: ').lower()
        tr_ans = ('no', 'yes')[is_prime(number)]
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
