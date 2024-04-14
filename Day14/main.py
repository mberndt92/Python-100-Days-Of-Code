
# Higher or Lower

import art
import game_data
import random


def next(previous):

    if previous is not None:
        first = previous
    else:
        first = random.choice(game_data.data)

    second = random.choice(game_data.data)
    return [first, second]


def print_challenge(challenge):
    first = challenge[0]
    second = challenge[1]
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")
    print(art.vs)
    print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}")


def evaluate_answer(challenge, answer):
    correct_answer = "A" if challenge[0]['follower_count'] > challenge[1]['follower_count'] else "B"
    return correct_answer == answer


def print_final_score(score):
    print(f"Game Over. Your final score is {score}")


def play_game(score):
    print(art.logo)
    previous = None

    while True:
        challenge = next(previous)
        print_challenge(challenge)
        choice = input("Who was more followers? Type 'A' or 'B': ")
        result = evaluate_answer(challenge, choice)

        if result:
            score += 1
        else:
            print_final_score(score)
            break


score = 0
play_game(score)