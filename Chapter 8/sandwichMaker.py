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
prices = {'Wheat': 2, 'White': 2, 'Sourdough': 2,
          'Chicken': 4, 'Turkey': 4, 'Ham': 4, 'Tofu': 5,
          'Cheddar': 1, 'Swiss': 1, 'Mozzarella': 1, 'no': 0,
          'Mayo': 0.1, 'Mustard': 0.1, 'Lettuce': 0.1, 'Tomato': 0.1}

BREAD_OPTIONS = ['Wheat', 'White', 'Sourdough']
PROTEIN_OPTIONS = ['Chicken', 'Turkey', 'Ham', 'Tofu']
CHEESE_OPTIONS = ['Cheddar', 'Swiss', 'Mozzarella']

totalCost = 0.0

# Greet user
print('Welcome to John & Julia\'s Sandwich & Sides! Let us make you a great sandwich!\n')

# Menu for bread type: wheat, white, or sourdough
promptBread = 'Which type of bread would you like?\n'
bread = pyip.inputMenu(BREAD_OPTIONS, prompt = promptBread, default = 'sourdough', limit = 3, numbered = True)
totalCost += prices[bread]

# Menu for protein type: chicken, turkey, ham, or tofu
promptProtein = 'Which type of protein would you like?\n'
protein = pyip.inputMenu(PROTEIN_OPTIONS, prompt = promptProtein, default = 'turkey', limit = 3, numbered = True)
totalCost += prices[protein]

# Yes/No for cheese type, then menu to specify:
# cheddar, Swiss, or mozzarella
promptCheeseYN = 'Would you like cheese on that? '
cheeseYN = pyip.inputYesNo(prompt = promptCheeseYN, limit = 3, default = 'yes')

if cheeseYN == 'yes':
    promptCheese = 'Which type of cheese would you like?\n'
    cheese = pyip.inputMenu(CHEESE_OPTIONS, prompt = promptCheese, default = 'Swiss', limit = 3, numbered = True)
else:
    cheese = 'no'

totalCost += prices[cheese]

# Yes/No for each mayo, mustard, lettuce, or tomato
print('Now for the toppings:')
mayo = pyip.inputYesNo(prompt = 'Mayo? (yes or no) ', limit = 3, default = 'yes')
if mayo == 'yes':
    totalCost += prices['Mayo']
    
mustard = pyip.inputYesNo(prompt = 'Mustard? (yes or no) ', limit = 3, default = 'yes')
if mustard == 'yes':
    totalCost += prices['Mustard']
    
lettuce = pyip.inputYesNo(prompt = 'Lettuce? (yes or no) ', limit = 3, default = 'yes')
if lettuce == 'yes':
    totalCost += prices['Lettuce']
    
tomato = pyip.inputYesNo(prompt = 'Tomato? (yes or no) ', limit = 3, default = 'yes')
if tomato == 'yes':
    totalCost += prices['Tomato']

# Int for how many sandwiches
promptSandwich = 'How many sandwiches would you like? '
number = pyip.inputInt(prompt = promptSandwich, limit = 3, min = 1, default = 1)
totalCost *= number

# Display order & total
print(f'Here\'s your order:\nBread: {bread}\nProtein: {protein}')
print(f'Cheese: {cheese}\nMayo: {mayo}\nMustard: {mustard}\nLettuce: {lettuce}\nTomato: {tomato}')
print(f'Your total will be ${totalCost:,.2f}\nPlease pay at the register.')