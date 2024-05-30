# There are 4 types of collection literals 1. List 2. Tuple 3. Set 4. Dictionary

# 1. List Literal
#    List is mutable. You can modify it or its content
numbers = [1, 3, 5, 7, 9]
numbers[0] = 2 # update value at index 0 to 2
numbers.append(11) # add value 11 at the end of the list
numbers.remove(5) # remove value 5
print(numbers)

# 2. Tuple Literal
#    Tuple is immutable. Cannot add new value or update its content
fruits = ('banana', 'orange', 'apple')
print(fruits[0])

# 3. Set Literal
dice_numbers = {1,2,3,4,5,6}
print(dice_numbers)

# 4. Dictaionary Literal
mai_nub = {1:'one', 2:'two'}
print(mai_nub[2])