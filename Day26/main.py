
# Nato Alphabet

import pandas


def generate_phonetic():
    user_input = input("What word do you need to translate to the nato alphabet? \n")
    try:
        output = [alphabet_dict[letter] for letter in user_input.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows() }
generate_phonetic()
