#!/usr/bin/env python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

"""
Project: Phone Number and Email Address Extractor
Say you have the boring task of finding every phone number and email
address in a long web page or document. If you manually scroll through
the page, you might end up searching for a long time. But if you had a
program that could search the text in your clipboard for phone numbers
and email addresses, you could simply press ctrl-A to select all the
text, press ctrl -C to copy it to the clipboard, and then run your
program. It could replace the text on the clipboard with just the
phone numbers and email addresses it finds.

Whenever you’re tackling a new project, it can be tempting to dive
right into writing code. But more often than not, it’s best to take a
step back and consider the bigger picture. I recommend first drawing
up a high-level plan for what your program needs to do. Don’t think
about the actual code yet — you can worry about that later. Right now,
stick to broad strokes.

For example, your phone and email address extractor will need to do
the following:
1. Get the text off the clipboard.
2. Find all phone numbers and email addresses in the text.
3. Paste them onto the clipboard.

Now you can start thinking about how this might work in code. The
code will need to do the following:
1. Use the pyperclip module to copy and paste strings.
2. Create two regexes, one for matching phone numbers and the other
    for matching email addresses.
3. Find all matches, not just the first match, of both regexes.
4. Neatly format the matched strings into a single string to paste.
5. Display some kind of message if no matches were found in the text.

This list is like a road map for the project. As you write the code,
you can focus on each of these steps separately. Each step is fairly
manageable and expressed in terms of things you already know how to do
in Python.
"""
import pyperclip, re

# 1. Use the pyperclip module to get text from clipboard
inputText = pyperclip.paste()

# 2. Create two regexes, one for matching phone numbers and the other
#    for matching email addresses.
findNum = re.compile(r"""(
    (?:\d{3}|\(\d{3}\))?      # Non-capturing group for area code
    (?:\s|-|\.)?              # Non-capturing group for spacer
    \d{3}                     # 3 digits
    (?:\s|-|\.)               # Non-capturing group for spacer
    \d{4}                     # 4 digits
    (?:\s*(?:ext|x|ext.)\s*\d{2,5})?  # Non-capturing group for extension
)""", re.VERBOSE)

findEmail = re.compile(r"""
[a-zA-Z0-9._%+-]+	# One or more of the allowed email characters
@	# The plain @ symbol
[a-zA-Z0-9.-]+	# One or more of the allowed domain characters
\.	# The plain . symbol
[a-zA-Z]{2,}	# Two or more letters for the TLD
""", re.VERBOSE)


# 3. Find all matches, not just the first match, of both regexes.
phNumbers = findNum.findall(inputText)
emails = findEmail.findall(inputText)

# 4. Neatly format the matched strings into a single string to paste.
matches = phNumbers + emails
if matches:
    outputText = ', '.join(matches)
else:
    outputText = ''

"""
outputText = ', '.join(phNumbers)
if not outputText:
    outputText = outputText + ', '.join(emails)
else:
    outputText = outputText + ', ' + ', '.join(emails)
"""

# 5. Display some kind of message if no matches were found in the text.
if not outputText:
    print('No matches found. Clipboard unchanged.')

# 6. Use Pyperclip to put the results back on the clipboard
else:
    pyperclip.copy(outputText)
    print(f'Found phone numbers: {len(phNumbers)}')
    print(f'Found emails: {len(emails)}')
    print('Results added to clipboard.')