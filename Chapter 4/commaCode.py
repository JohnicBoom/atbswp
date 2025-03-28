# Write a function that takes a list value as an argument and returns
# a string with all of the items separates by a comma and a space,
# with 'and' inserted before the last item.
# Should work with any value, including an empty list [].

# Receive a list, return a string

# Separate issues to solve for:
#	Empty list
#	One item
#	Two items
#	Many items

def comma(list):
# Is the list empty?
# Return an empty string
    if len(list) == 0:
        return 'Empty list!'
# Does the list only have one item?
# Return that item
    elif len(list) == 1:
        return list[0]
# does the list have two items?
# Return a string with index 0 'and' index 1
    elif len(list) == 2:
        return list[0] + ' and ' + list[1]
# Does the list have three or more items?
# Slice list to get items that will only be separated by commas
# Loop that adds each item to a string, separated by commas
# Add the final item, separated by ', and', to the string
# Return the complete string
    else:
        string = ''
        first = list[:-1]
        for i in range(len(first)):
            string = string + list[i] + ', '
        string = string + 'and ' + list[-1]
        return string
spam = []
print(comma(spam))