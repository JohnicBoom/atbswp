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

def regexStrip(inputText, removeChars):
    
    # If removeChars is empty, remove whitespace characters from inputText
    # but leave inner whitespace intact
        # regex that matches any string starting with space
        # if I get a match, remove first char, then check again
        # if no match, move on to checking the end for space
        # if I get a match, remove last char (length of string - 1)
        
        
        # RegEx match
        removal = re.compile(r"""
            ^(^\s)			# begins with non-space character
            .*				# contains anything
            \S$				# ends with non-space character
                             """, re.VERBOSE)
        
    
    
    # If removeChars is received, remove those characters from inputText