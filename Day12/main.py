
# Number Guessing Game
import random

def print_lives(lives):
    print(f"You have {lives} attempts remaining to guess the number")


lives = 5
random_number = random.randint(1, 101)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    lives = 10

print_lives(lives)

while lives > 0:
    guess = int(input("Make a guess: "))
    if guess < random_number:
        print("Too low.")
        lives -= 1
        print_lives(lives)
    elif guess > random_number:
        print("Too high.")
        lives -= 1
        print_lives(lives)
    else:
        break

print(f"The number was: {random_number}")
if lives == 0:
    print("You lose.")
else:
    print("You win")
