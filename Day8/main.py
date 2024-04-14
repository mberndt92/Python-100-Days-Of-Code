# Caesar Cipher
import art
def caesar(message, shift, direction):
    shifted_message = ""
    for pos in range(0, len(message)):
        index = alphabet.index(message[pos])
        if direction == "encode":
            new_index = (index + shift) % len(alphabet)
        else:
            new_index = (index - shift)
        shifted_message += alphabet[new_index]
    return shifted_message


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    print(f"Your {direction}d message is: {caesar(message=text, shift=shift_amount, direction=direction)}")

    choice = input("Do you want to re-run the program? (y/n) \n")
    if choice == "n":
        break
