#!/usr/bin/env python3
# dateDetection.py - Detect dates in DD/MM/YYYY format and check if they are valid

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

import re, pyperclip

# Get data from clipboard with pyperclip
inputText = pyperclip.paste()

# RegEx to extract the dates
getDates = re.compile(r"""
[0123]\d		# day
/				# divider
[01]\d			# month
/				# divider
\d\d\d\d		# year
""", re.VERBOSE)

# Extract the dates into a list
dates = getDates.findall(inputText)
print(dates)
# Loop through the list - ['29/10/1982', '25/09/1973']
for date in dates:
    # separate date into 'month', 'day', 'year' variables
    day, month, year = date[0:2], date[3:5], date[6:]
		# validate day for month
 		# if month is February, check for Leap year
    if 1000 < int(year) < 2999:
        if month == '00':
            valid = 'not a valid date'
        if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
            if 0 < int(day) < 32:
                valid = 'valid'
            else:
                valid = 'not a valid date'
        if month == '04' or month == '06' or month == '09' or month == '11':
            if 0 < int(day) < 31:
                valid = 'valid'
            else:
                valid = 'not a valid date'
        if month == '02':
            if (int(year) % 4 == 0) and (int(year) % 100 !=0 or int(year) % 400 == 0):
                if 0 < int(day) < 30:
                    valid = 'valid'
                else:
                    valid = 'not a valid date'
            else:
                if 0 < int(day) < 29:
                    valid = 'valid'
                else:
                    valid = 'not a valid date'
    else:
        valid = 'not a valid date'
#	print date and whether it is valid
    print(f'{date} is {valid}.')