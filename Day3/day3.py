# Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."-` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("You're at a cross road. Where do you want to go? (left or right) -> ")

# simplified it for a non-nested flow
if left_or_right.lower() != "left":
    print("You fell into a hole. Game Over.")
    exit()

swim_or_wait = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                     'boat. Type "swim" to swim across. -> ')

if swim_or_wait.lower() != "wait":
    print("You are attacked by a giant Wulliwustruppi. Game Over.")
    exit()

door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
             "Which colour do you choose? -> ")
if door.lower() == "red":
    print("The Red Ribbon Army has a comeback. Their first victim: You. Game Over.")
    exit()
elif door.lower() == "blue":
    print("You fall into a giant pool of water. The inhabitant of the aquarium you entered is not happy with your "
          "presence. You become shark food. Game Over")
    exit()
elif door.lower() == "yellow":
    print("You found the treasure. Who would've thought! You Win!")





