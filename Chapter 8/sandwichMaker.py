#!/usr/bin/env python3
# sandwichMaker.py - Take a sandwich order


'''
Write a program that asks users for their sandwich preferences.
The program should use PyInputPlus to ensure that they enter
valid input, such as:
* Using inputMenu() for a bread type: wheat, white, or sourdough.
* Using inputMenu() for a protein type: chicken, turkey, ham, or
  tofu.
* Using inputYesNo() to ask if they want cheese.
  If so, using inputMenu() to ask for a cheese type:
  cheddar, Swiss, or mozzarella.
* Using inputYesNo() to ask if they want mayo, mustard, lettuce,
  or tomato.
* Using inputInt() to ask how many sandwiches they want. Make
  sure this number is 1 or more.
* Come up with prices for each of these options, and have your
  program display a total cost after the user enters their
  selection.
'''

# include modules
import pyinputplus as pyip

# Create price dictionary for each menu option & start total cost
# at $0
prices = {'wheat': 2, 'white': 2, 'sourdough': 2,
          'chicken': 4, 'turkey': 4, 'ham': 4, 'tofu': 5,
          'cheddar': 1, 'Swiss': 1, 'mozzarella': 1,
          'mayo': 0.1, 'mustard': 0.1, 'lettuce': 0.1, 'tomato': 0.1}

totalCost = 0.0

# Greet user
print('Welcome to John & Julia\'s  Sandwich & Sides! Let us make you a great sandwich!\n')

# Menu for bread type: wheat, white, or sourdough
promptBread = 'Which type of bead would you like?\n'
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt = promptBread, default = 'sourdough', limit = 3, numbered = True)

# Menu for protein type: chicken, turkey, ham, or tofu
promptProtein = 'Which type of protein would you like?\n'
meat = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt = promptProtein, default = 'turkey', limit = 3, numbered = True)

# Yes/No for cheese type, then menu to specify:
# cheddar, Swiss, or mozzarella
promptCheeseYN = 'Would you like cheese on that?'
cheeseYN = pyip.inputYesNo(prompt = promptCheeseYN, limit = 3, default = 'yes')

# Yes/No for each mayo, mustard, lettuce, or tomato


# Int for how many sandwiches

# Calculate & display total