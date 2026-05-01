# Day 2 — Tip Caltulator
# Angela Yu's 100 Days of Code
# Asks user for city, bill and people and calculate how much they must pay

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_with_tip = bill * (1 + tip / 100)
each_pays = total_with_tip / people

print(f"Each person should pay: ${each_pays:.2f}")
