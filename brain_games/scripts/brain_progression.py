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
        tr_ans = progression[index_answer]
        progression[index_answer] = '..'
        question = ' '.join(progression)
        print(f'Question: {question}')
        ans = input('Your answer: ')
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
