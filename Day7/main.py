
# Hangman
import random
import hangman_ascii_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

print(hangman_ascii_art.logo)

display = list()
for _ in chosen_word:
    display.append("_")

lives = 6

guessed_letters = []

while lives > 0 and "_" in display:
    guess = input("Choose a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter :)")
        continue
    guessed_letters.append(guess)
    is_valid = False

    for position in range(0, len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            is_valid = True

    if not is_valid:
        lives -= 1
        print(hangman_ascii_art.stages[lives])
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(''.join(display))

if lives == 0:
    print(f"You lose - the solution was {chosen_word}")
else:
    print("You win")