# Blackjack

import random

# simple & infinite deck assumption
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(cards)


def calculate_score(cards):
    score = 0
    for value in cards:
        score += value
    return score


def print_player_score(player):
    score = calculate_score(player)
    print(f"Your cards: {player}, current score: {score}")


def print_dealer_score(dealer):
    score = calculate_score(dealer)
    print(f"Computer's score: {score}")


def play_dealer_turn(dealer):
    while calculate_score(dealer) < 17:
        dealer.append(draw_card())
    return dealer


def player_turn(player):
    draw_more = True
    while draw_more:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == 'y':
            player.append(draw_card())
            print_player_score(player)
            if calculate_score(player) > 21:
                draw_more = False
        else:
            draw_more = False
    return player


def print_score(player, dealer):
    print_player_score(player)
    print_dealer_score(dealer)


def play_game():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card()]
    print_score(player_hand, dealer_hand)

    player_hand = player_turn(player_hand)

    if calculate_score(player_hand) <= 21:
        dealer_hand = play_dealer_turn(dealer_hand)
    else:
        print("You went over. You lose")

    print_dealer_score(dealer_hand)

    if calculate_score(dealer_hand) > 21:
        print("The dealer went over. You win")
    else:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        if player_score > dealer_score:
            print("You win.")
        elif player_score == dealer_score:
            print("Draw.")
        else:
            print("You lose.")


while True:
    play_game()
    choice = input("Play another game? (y/n): \n").lower()
    if choice == "n":
        break
