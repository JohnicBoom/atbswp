# You are creating a fantasy video game. The data structure to model
# the player’s inventory will be a dictionary where the keys are
# string values describing the item in the inventory and the value is
# an integer value detailing how many of that item the player has.
# For example, the dictionary value
# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.
#
# Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
#
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62
#
# Hint: You can use a for loop to loop through all the keys in a
# dictionary.
#
#
#
# Create the inventory dictionary
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# Define the display function
def displayInventory(inventory):
    # Print a heading
    print("Inventory:")
    # Initialize total item counting variable
    item_total = 0
    # Loop through the dictionary
    for k, v in inventory.items():
        # Print the number of this item held, then the item name
        print(f"{v} {k}")
        # Add that number to our total item count
        item_total += v
    # Print total item count
    print(f"Total number of items: {item_total}")
# Call the function
displayInventory(stuff)