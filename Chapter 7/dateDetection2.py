#!/usr/bin/env python3
# dateDetection2.py - Detect dates in DD/MM/YYYY format and check if they are valid

"""
Date Detection
Write a regular expression that can detect dates in the DD/MM/YYYY for-
mat. Assume that the days range from 01 to 31, the months range from 01
to 12, and the years range from 1000 to 2999. Note that if the day or month
is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each
month or for leap years; it will accept nonexistent dates like 31/02/2020 or
31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April,
June, September, and November have 30 days, February has 28 days, and
the rest of the months have 31 days. February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly divis-
ible by 100, unless the year is also evenly divisible by 400. Note how this cal-
culation makes it impossible to make a reasonably sized regular expression
that can detect a valid date.
"""

"""
Trying this one again with a regex that filters most of the invalid
dates already, uses a dictionary for days-in-the-month, and some other
alternatives I want to try, thanks to a code review from Grok3 on my
original attempt.
"""

import re, pyperclip

# Get data from clipboard
inputText = pyperclip.paste()

# RegEx to extract dates
# day = 01-31, month = 01-12, year = 1000-2999
# Group days, months, years
getDates = re.compile(r"""
(0[1-9]|[12]\d|3[01])	# day grouping
/						# separater
(0[1-9]|1[012])			# month grouping
/						# separater
([12]\d\d\d)			# year grouping
""", re.VERBOSE)

# Put dates in a list, handle an empty list/no matches
dates = getDates.findall(inputText)
if not dates:
    print('There were no dates found with the correct format.')

# Leap year check function - returns True or False
def isLeap(year):
    if (year % 4 == 0) and (year % 100 !=0 or year % 400 == 0):
        return True
    else:
        return False

# Dictionary for month lengths
daysInMonth = {'01': 31, '02': 28, '03': 31, '04': 30,
               '05': 31, '06': 30, '07': 31, '08': 31,
               '09': 30, '10': 31, '11': 30, '12': 31}

# Validate Dates
# Loop through list of tuples
for date in dates:
# Unpack the tuple into my variables (day, month, year)
    day, month, year = date
# Convert day & year to int
    day, year = int(day), int(year)
# Set var for max days in month
    maxDays = daysInMonth[month]
# Adjust for Feb if leap year
    if month == '02':
        if isLeap(year) == True:
            maxDays = 29
    # Validate day and print result
    if 0 < day <= maxDays:
        valid = True
    else:
        valid = False
    if valid:
        print(f'{day}/{month}/{year} is valid.')
    else:
        print(f'{day}/{month}/{year} is not a valid date.')
        
# Print confirmation that program is finished
print(f'\nSuccessfully validated {len(dates)} dates.')

# Test dates
# 29/10/1982 29/02/2020 29/02/2023