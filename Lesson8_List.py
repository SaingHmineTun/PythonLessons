# List is an ordered sequence of items and it's flexible
# A list can store many types of data
mix = [1, 2.5, True, 'Mao']
print(mix, mix[2])

# slicing a list
print(mix[1:3]) # show from index1 to excluding index3

# knowing the length of the list
print(len(mix))

# another way to create a list in python
numbers = list((2, 4, 6, 8, 10))
print(numbers)

# Negative Indexing in list
print(numbers[-1]) # The last item in a list
print(numbers[-2]) # The second last item in a list

# Insert item at specified index
numbers.insert(0, 1)
print(numbers)

# Add item at the end of the list
numbers.append(12)
print(numbers)

# Add another list to current list
odd_numbers = [1, 3, 5, 7, 9]
numbers.extend(odd_numbers)
print(numbers)

# Remove item from list
numbers.remove(5)
print(numbers)

# Pop method removes the item at the specified index or if index is not defined, remove the item at last index
numbers.pop(0)
print(numbers)

# Remove the item at specified index with del function
del numbers[2]
print(numbers)

# Clear the list
numbers.clear()
print(numbers)