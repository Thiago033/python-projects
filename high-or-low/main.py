import os
import random
from art import logo, vs
from gamedata import data

clear = lambda: os.system('cls')


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


def check_answer(guess, a, b):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)

    score = 0
    continue_game = True

    account_b = get_random_account()

    while continue_game:

        account_a = account_b
        account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        follows_a = account_a["follower_count"]
        follows_b = account_b["follower_count"]

        is_correct = check_answer(guess, follows_a, follows_b)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
