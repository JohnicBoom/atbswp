#!/usr/bin/env python3
# bulletPointAdder.py - add bullet points to the beginning of each
# line of text on clipboard

import pyperclip

# Get text from the clipboard
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')

# Loop through all indicies in the "lines" list
for index in range(len(lines)): 
    # add star to each string in "lines" list
    lines[index] = '* ' + lines[index]

# Join the list items back into one string, separated by newlines
text = '\n'.join(lines)

# Put text back on the clipboard
pyperclip.copy(text)