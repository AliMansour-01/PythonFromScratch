#control flow and logical operators

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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
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

choice_1 = input("You're at a cross road. where do you want to go? Type 'left' or 'right ")
if choice_1.lower() == "left":
    choice_2 = input("You have come to a lake. Thee is an island in the middle of the lake. type wait to 'wait' for a "
                     "boat. Type swim to 'swim' across ")
    if choice_2.lower() == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and "
                         "one blue. Which color do you choose ")
        if choice_3.lower() == "Yellow":
            print("You win!")
        elif choice_3.lower() == "Red":
            print("Burned by fire. Game over")
        elif choice_3.lower() == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")