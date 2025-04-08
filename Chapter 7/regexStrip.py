#!/usr/bin/env python3
# regexStrip2.py - regex version of the strip() method

"""
Write a function that takes a string and does the same thing as
the strip() string method. If no other arguments are passed other
than the string to strip, then whitespace characters will be
removed from the beginning and end of the string. Otherwise, the
characters specified in the second argument to the function will
be removed from the string.
"""

import re

def regexStrip(inputText, rmChars = r'\s'):

    # Copy inputText to working string for non-destructive work
    cleanText = inputText
    
    # Put the characters in a regex class by wrapping with []
    rmChars = '[' + rmChars + ']'
                
    # Regex that matches any string starting with rmChars
    removalS = re.compile('^' + rmChars)
    # Regex that matches any string ending with rmChars
    removalE = re.compile(rmChars + '$')
    
    # If I get a match, remove first char, then check again
    match = removalS.findall(cleanText)
    while match:
        cleanText = cleanText[1:]
        match = removalS.findall(cleanText)

    # If no match, move on to checking the end for rmChars
    match = removalE.findall(cleanText)
    # If I get a match, remove last char and check again
    while match:
        cleanText = cleanText[0:len(cleanText) - 1]
        match = removalE.findall(cleanText)
    
    return cleanText

# Tests
test = '   This is a test  '
print(f'Original text: "{test}"\nCleaned text:  "{regexStrip(test)}"')

test = 'spamTest text herespam'
print(f'Original text: "{test}"\nCleaned text:  "' + regexStrip(test, 'maps') + '"')

test = ' \n This\nis\na\ntest \n '
print(f'Original text: "{test}"\nCleaned text:  "{regexStrip(test)}"')

test = '234Test567'
print(f'Original text: "{test}"\nCleaned text:  "' + regexStrip(test, r'\d') + '"')

test = 'qwerty123 Test Text 456asdfg'
print(f'Original text: "{test}"\nCleaned text:  "' + regexStrip(test, r'\w') + '"')
