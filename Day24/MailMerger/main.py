
with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as ready_to_send:
        ready_to_send.write(new_letter)

