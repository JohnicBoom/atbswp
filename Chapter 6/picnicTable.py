def printPicnic(itemsDict, leftWidth, rightWidth):
    # Print title
    print('\n' + ('*' * (leftWidth + rightWidth)) + '\n')
    print(f'{"PICNIC ITEMS".center(leftWidth + rightWidth, "-")}')
    
    for item, number in itemsDict.items():
        print(f'{item.ljust(leftWidth, ".")} {str(number).rjust(rightWidth)}')
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)