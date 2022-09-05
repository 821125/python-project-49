#!/usr/bin/env pyhton3
from brain_games.cli import get_progression, greeting, welcome_user
from random import randint


def main():

    greeting()
    name = welcome_user()

    print('What number is missing in the progression?')

    count = 0
    while count < 3:
        progression = get_progression()
        index_answer = randint(2, 7)
        true_answer = progression[index_answer]
        progression[index_answer] = '..'
        question = ' '.join(progression)
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer == true_answer:
            print("Correct!")
            count += 1
        else:
            print(f"{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print(f"Let's try, again, {name}!")

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
