#!/usr/bin/env python3
# strPass.py - Strong Password Detection

"""
Write a function that uses regular expressions to make sure the
password string it is passed is strong. A strong password is
defined as one that is at least eight characters long, contains
both uppercase and lowercase characters, and has at least one
digit. You may need to test the string against multiple regex
patterns to validate its strength.
"""

import re

def validatePassword(passw):

    # Regular expression using "positive lookahead assertions"
    test = re.compile(r"""
    (?=.*[A-Z])		# Uppercase letter
    (?=.*[a-z])		# Lowercase letter
    (?=.*[\d])		# Digit
    .{8,}
    """, re.VERBOSE)
    
    # If there is a match, the password is strong enough
    if test.search(passw):
        print('That is a strong password.')
        return True
    else:
        print('Weak password. Please try again.')
        return False

# Test function
validatePassword('123456qwER')
validatePassword('12345678qW')
validatePassword('qwertyuiop')
validatePassword('q1W2eR9sR')
