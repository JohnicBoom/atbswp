# Function collatz()
# Takes number, returns (number // 2) for evens, (3 * number + 1) for odds

# Get input (as int, not string). Call collatz() and print return until
# we get to 1

# Hint:
#	even: number % 2 == 0
#	odd: number % 2 == 1

import sys, time

def collatz(userNumber):
    if userNumber % 2 == 0:
        return userNumber // 2
    elif userNumber % 2 == 1:
        return 3 * userNumber + 1
    
try:
    while True:
        print('Please enter a number: ', end='')
        try:
            userNum = int(input())
            while userNum != 1:
                userNum = collatz(userNum)
                print(userNum)
                time.sleep(0.2)
            print('We made it!')
            print('')
        except ValueError:
             print('This only works with numbers')
             print('')
except KeyboardInterrupt:
    sys.exit()