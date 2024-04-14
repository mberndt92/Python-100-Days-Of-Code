
# Silent Auction

import os
import logo

print(logo.logo)

bidders = []

while True:

    name = input("What's your name? \n")
    bid = int(input("What's your bid? \n"))

    bidders.append({
        "name": name,
        "bid": bid
    })

    more_bidders = input("Are there any other bidders? (Yes/No) \n").lower()
    if more_bidders == "no":
        break
    else:
        os.system('clear')

highest_bidder = ""
highest_bid = 0
for bidder in bidders:
    if bidder["bid"] > highest_bid:
        highest_bid = bidder["bid"]
        highest_bidder = bidder["name"]

print(f"The highest bidder was {highest_bidder} with ${highest_bid}")