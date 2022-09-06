#!/usr/bin/env pyhton3
from brain_games.cli import greeting, welcome_user
from random import randint


def main():

    def check_even(answer):
        return answer % 2 == 0

    greeting()
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        number = randint(1, 99)
        print(f'Question: {number}')
        answer = input('Your answer: ').lower()
        true_answer = ('no', 'yes')[check_even(number)]
        if answer == true_answer:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print(f"Let's try, again, {name}!")

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
