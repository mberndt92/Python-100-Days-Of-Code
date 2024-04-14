import random

# Rock, Paper, Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

results = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0]
]

icons = [rock, paper, scissors]

print(icons[choice])
print("\n")
print("Computer chose: \n")
print(icons[computer])

result = results[choice][computer]
if result == 0:
    print("Its a draw.")
elif result == -1:
    print("You lose.")
elif result == 1:
    print("You win.")