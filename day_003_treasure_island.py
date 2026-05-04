# Day 3 — Treasure Island
# Angela Yu's 100 Days of Code
# The text game

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
first_choice = input('You\'re at a cross road. You want go "left" or "right"? ')
if first_choice == "left":
    second_choice = input('You\'ve come to a lake. There is an island in the middle of the lake. You wanna "wait" for boat or "swim" across the lake ')
    if second_choice == "wait":
        third_choice = input("You arrive at the island. There is a cave with 3 patches. One is all with the blue mushrooms(blue), one completely dark(black) and one with torches(yellow). Which patch you choose? ")
        if third_choice == "blue":
            print("Eaten by vampire gnomes. Game Over.")
        elif third_choice == "black":
            print("Your eyes adjust to the dark. You see a golden reflection at the end of the tunnel — it's a treasure! GG! You Win!")
        else:
            print("You get shot by an arrow trap. Game Over")
    else:
        print("Attacked by trout. Game Over")
else :
    print("Fall into a hole. Game Over.")
