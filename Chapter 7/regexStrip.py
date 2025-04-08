#!/usr/bin/env python3
# regexStrip.py - regex version of the strip() method

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
    
    # If rmChars has more than one character, I need to add |
    # and ^ or $
    if len(rmChars) > 1 and (rmChars != r'\s' and rmChars != r'\d' and rmChars != r'\w'):
        rmCharsS = rmChars[0]
        for i in range(len(rmChars) - 1):
            rmCharsS = rmCharsS + '|^' + rmChars[i+1]
            
        rmCharsE = rmChars[0]
        for i in range(len(rmChars) - 1):
            rmCharsE = rmCharsE + '$|' + rmChars[i+1]
    else:
        rmCharsS, rmCharsE = rmChars, rmChars
        
                
    # Regex that matches any string starting with rmChars
    #removalS = re.compile('^' + rmChars + '.*', re.DOTALL)
    removalS = re.compile('^' + rmCharsS)
    # Regex that matches any string ending with rmChars
    #removalE = re.compile('.*' + rmChars + '$', re.DOTALL)
    removalE = re.compile(rmCharsE + '$')
    
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
    
    # Print final cleaned string
    #print(f'Original text was: "{inputText}"')
    #print(f'Stripped text is: "{cleanText}"')
    
    return cleanText

# Test
test = '   This is a test  '
print(f'Original text: "{test}"\nCleaned text:  "{regexStrip(test)}"')

test = 'spamTest text herespam'
print(f'Original text: "{test}"\nCleaned text:  "' + regexStrip(test, 'maps') + '"')

test = ' \n This\nis\na\ntest \n '
print(f'Original text: "{test}"\nCleaned text:  "{regexStrip(test)}"')
# regexStrip(' \n This\nis\na\ntest \n ')

test = '234Test567'
print(f'Original text: "{test}"\nCleaned text:  "' + regexStrip(test, r'\d') + '"')
#regexStrip('234Test567', '\d')

test = 'qwerty123 Test Text 456asdfg'
print(f'Original text: "{test}"\nCleaned text:  "' + regexStrip(test, r'\w') + '"')