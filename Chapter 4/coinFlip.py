# Find out how often a streak of six heads or six tails comes up in a
# randomly generated list of 100 values.
#
# Two parts: generate the list of 'heads' and 'tails' values, and then
# check for streaks of 6.
#
# Run 10,000 times and keep track of streaks

# import necessary libraries
import random
# Initialize streak variable
numberOfStreaks = 0
gamesWithStreak = 0
# Loop 10,000 times
for experimentNumber in range(10000):
# Create a 100-item list
#	Loop 100 times
#	Store coin-flip result in next list index
    flipRecord = []
    for flipNumber in range(100):
        coinFlip = random.randint(0, 1)
        if coinFlip == 0:
            flipRecord.append('heads')
        if coinFlip == 1:
            flipRecord.append('tails')
# Find streaks of 6
#	Check to see if the next flip matches this one.
#	If it does, add one to 'streak', check the next pair
#	If it doesn't, clear streak, check the next pair
#	If 'streak' gets to 6, add one to numberOfStreaks, clear 'streak'
    streak = 1
    hasStreak = False
    for streakChecker in range(len(flipRecord) - 1):
    # Check for matching flips
        if flipRecord[streakChecker] == flipRecord[streakChecker + 1]:
            streak += 1
        else:
            streak = 1
    # Check for streak of 6
        if streak == 6:
            numberOfStreaks +=  1
            hasStreak = True
            streak = 1
    if hasStreak == True:
        gamesWithStreak += 1
# Print the results
print('Number of streaks of 6: ' + str(numberOfStreaks))
print('Chance of streak: %s%%' % ((gamesWithStreak / 10000) * 100))