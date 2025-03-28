# This program should print Hello for 1, Howdy for 2, Greetings for anything else, quit with q
import sys

while True:
    userEntry = input()
    if userEntry == '1':
        print('Hello')
    elif userEntry == '2':
        print('Howdy')
    elif userEntry == 'q':
        sys.exit()
    else:
        print('Greetings')