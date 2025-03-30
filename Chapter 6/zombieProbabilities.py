#!/usr/bin/env python3
# zombieProbabilities.py - show probabilities of die roles in the game Zombie Dice

"""
Shotgun = S, Brains = B, Footsteps = F

3 red dice - S more likely		3S 2F 1B	0.5 0.333 0.167
4 yellow dice - B & S even		2S 2F 2B	0.333
6 green dice - B more likely	1S 2F 3B	0.167 0.333 0.5

P of S with 3 green dice:
    1 - .833 x .833 x .833 = 0.42199 = 42.199%

"""


# Create a list
# Append to that list, an item that is a three-item list of dice
# threeDice = []
dColor = ['red', 'yellow', 'green']

# Give probability for color
def getProb(color):
    redp, yellowp, greenp = 0.5, 0.666, 0.833
    if color == 'red':
        return redp
    if color == 'yellow':
        return yellowp
    if color == 'green':
        return greenp
    else:
        return 0

"""
# Nested loop method
for first in range(len(dColor)):
    for second in range(len(dColor)):
        for third in range(len(dColor)):
            threeDice.append([dColor[first], dColor[second], dColor[third]])
"""
# list comprehension method
threeDice = [[first, second, third] for first in dColor for second in dColor for third in dColor]
threeDiceProbs = {}
# List unpacking to loop through list
for die1, die2, die3 in threeDice:
    prob1 = getProb(die1)
    prob2 = getProb(die2)
    prob3 = getProb(die3)
    setProb = round((1 - prob1 * prob2 * prob3) * 100, 3)
    print(f'{die1}, {die2}, {die3} = {setProb}%')
    colorCombo = f'{die1}, {die2}, {die3}'
    threeDiceProbs[colorCombo] = setProb







"""
# initialize dice cup
cup = ['red', 'red', 'red', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green']
random.shuffle(cup)


print(f'Cup has this many dice: {len(cup)}')
roll = cup[0:3]
cup = cup[3:]
print(f'Roll = {roll}')
print(f'Remaining cup has this many dice: {len(cup)}')


# Calculate probability of rolling at least 1 S on this roll
probs = []
for i in range(len(roll)):
    probs.append(getProb(roll[i]))
print(probs)
prob = 1 - probs[0] * probs[1] * probs[2]
print(f'The probability of 1 or more S is: {prob} or {prob * 100}%')

"""