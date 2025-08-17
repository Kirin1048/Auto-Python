print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice1 = input('You are at a crossroad, where do you go? Type left or right.').lower()

if choice1 == "left":
    choice2 = input("You've come to a clearing, there is a pack of what appears to be herbivores grazing. Do you wait or approach?").lower()
    if choice2 == "wait":
        choice3 = input("Now the creatures are out of the clearing you have a better view \n There are 3 huts; one red, one blue, and one yellow. Which do you choose?").lower()
        if choice3 == "yellow":
            print("You find the gold, and have won the game!")
        elif choice3 == "red":
            print("You enter the house, and it is a trap. Game Over")
        else:
            print ("It was a trap. Game Over")
    else:
        print("They are not herbivores, you are lunch. Game Over")
else:
    print("You found a pack of wild monsters and became lunch. Game Over.")