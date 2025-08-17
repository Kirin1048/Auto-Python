import random

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

computer_choice = random.randint(0,2)
#computer_gesture = 0

player_string = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors")
player_int = int(player_string)
#player_gesture = 0

if  player_int == 0:
    print(rock)
elif player_int == 1:
    print(paper)
elif player_int == 2:
    print(scissors)
# else:
#     print("You cheat and lose")

print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if player_int == 0 and computer_choice == 1:
    print("You lose")
elif player_int == 1 and computer_choice == 2:
    print("You lose")
elif player_int == 2 and computer_choice == 0:
    print("You lose")
elif player_int == 0 and computer_choice == 2:
    print("You win")
elif player_int == 1 and computer_choice ==0:
    print("You win")
elif player_int == 2 and computer_choice ==1:
    print("You win")
else:
    print("It is a tie")






