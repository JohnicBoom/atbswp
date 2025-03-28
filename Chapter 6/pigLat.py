#!/usr/bin/env python3
# pigLat.py - Translate input to Pig Latin

# Get the message we want to translate
print('Enter the English message to translate into Pig Latin:')
message = input()

# Create a tuple of the vowels so we can determine when words start
# with one
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

# Create the list for our translated words
pigLatin = []

# Split 'message' into individual words by whitespace
for word in message.split():
    # Separate the non-letters at the start of the word
    prefixNonLetters = ''
    # If first character in 'word' is non-alpha, add it to the end of
    # 'prefixNonLetters'. Remove that character from the beginning
    # of 'word' and then test the new first character in 'word'
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
        
    # If the word was entirely non-alpha, write it as the next list-
    # item in our 'pigLatin' list
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    
    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    
    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    # Make the word lowercase for translation.
    word = word.lower() 
    
    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    
    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
        
    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
        
    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
    
# Join all the words back together into a single string:
print(' '.join(pigLatin))