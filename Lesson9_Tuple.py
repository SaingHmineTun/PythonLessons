# It's an ordered of items just like list
# The only difference is that tuple is immutable
mix = (10, 'Mao', 13.25)
print(mix)

# Accessing tuple value
print(mix[1])

# Know the length of tuple
print(len(mix))

# Create tuple with a single item
numbers = (1,)
print(type(numbers))

# Convert tuple to a list
numbers = list(numbers)
print(type(numbers))

# Tuple unpacking is also possible
aTuple = "Yellow", 20, "Red"
print(aTuple)