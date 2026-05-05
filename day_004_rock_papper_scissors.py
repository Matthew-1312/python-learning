# Day 4 — Rock Paper Scissors
# Angela Yu's 100 Days of Code
# Player picks rock/paper/scissors, computer chooses randomly, winner is decided.

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
computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_choice >= 3 or user_choice < 0:
    print("Invalid number, you lose!")
else:

    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)

    if computer_choice == 0:
        print(f"Computer chose:\n{rock}")
    elif computer_choice == 1:
        print(f"Computer chose:\n{paper}")
    elif computer_choice == 2:
        print(f"Computer chose:\n{scissors}")

    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == user_choice - 1:
        print("You win!")