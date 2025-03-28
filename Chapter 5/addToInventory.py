# Imagine that a vanquished dragon’s loot is represented as a list of
# strings like this:
#
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Write a function named addToInventory(inventory, addedItems), where
# the inventory parameter is a dictionary representing the player’s
# inventory (like in the previous project) and the addedItems
# parameter is a list like dragonLoot. The addToInventory() function
# should return a dictionary that represents the updated inventory.
# Note that the addedItems list can contain multiples of the same item.
# Your code could look something like this:
#
# def addToInventory(inventory, addedItems):
    # your code goes here
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)
#
# The previous program (with your displayInventory() function from the previous project)
# would output the following:
#
# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# 
# Total number of items: 48
#
####################################################################
#
# Define function
def addToInventory(inventory, addedItems):
    # Loop through addedItems
    for item in addedItems:
        # Check for the item. Add if not there, add 1 if it is
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

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

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)