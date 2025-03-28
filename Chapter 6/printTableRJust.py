#!/usr/bin/env python3
# printTableRJust.py - Print a list of lists as a pretty table

"""Write a function named printTable() that takes a list of lists of
strings and displays it in a well-organized table with each column
right-justified. Assume that all the inner lists will contain the same
number of strings.

For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
  
Hint: your code will first have to find the longest string in each of
the inner lists so that the whole column can be wide enough to fit all
the strings.

You can store the maximum width of each column as a list of integers.
The printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the
number of inner lists in tableData. That way, colWidths[0] can store
the width of the longest string in tableData[0], colWidths[1] can
store the width of the longest string in tableData[1], and so on.
You can then find the largest value in the colWidths list to find out
what integer width to pass to the rjust() string method."""

# Define the function
def printTable(tableData):

    # Create colWidths[] with enough items to match the number of lists
    colWidths = [0] * len(tableData)
    
    # Set colWidths[] list items to the right size
    # For each sub-list in the main list
    for sublist in range(len(tableData)):
        # For each item in the sub-list
        for item in tableData[sublist]:
            # Check if the length of this string is > colWidths[sub-list]
            itemLength = len(item)
            if itemLength > colWidths[sublist]:
                # Save length of string to colWidths[sub-list]
                colWidths[sublist] = itemLength
                
    # For each item in a sub-list (rows)
    for row in range(len(tableData[0])):
        # For each list (columns)
        for col in range(len(tableData)):
            # Print the item right-justified, no line-break
            print(tableData[col][row].rjust(colWidths[col] + 1), end = '')
        # Line break between rows
        print('')
    
# Test
testTable = [['apples', 'oranges', 'cherries', 'banana', 'grape'],
['Alice', 'Bob', 'Carol', 'David', 'John'],
['dogs', 'cats', 'moose', 'goose', 'duck']]
printTable(testTable)