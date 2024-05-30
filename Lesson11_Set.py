# Set is unordered and can only contain unique items
keys = {1, 3, 2, 4, 8, 10, 4}
print(keys)

fruits = {"apple", "watermelon", "banana", "mango"}
print(fruits)

# Accessing set items
for f in fruits:
    print(f)
    

# Adding new item into set
fruits.add('Strawberry')
print(fruits)

# Remove item from set
# fruits.remove('appl') # Throw error if not exist
print(fruits)

# Remove item from set
fruits.discard('appl') # If not exist, will not throw error


# Remove random item from set
fruit = fruits.pop()
print(fruit, "is removed!", fruits)

# Clear the entire set
fruits.clear()
print(fruits)

# WORKING WITH 2 SETS
# The difference_update() method removes the items that exist in both sets. Here set1.difference_update(set2) so it removed the unwanted items from the original set1.
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}
 
set1.difference_update(set2)
print(set1)

# Set Union
# The union() method returns a new set with all items from both sets by removing duplicates

set3 = set1.union(set2)
print(set3)
