# Using index placeholder
introduction = 'Hello, my name is {0}'.format('Sai Mao')
print(introduction)

# Using keyword arg to format
message = 'Actually, I am {age} years old and I am from {city}, {country}'.format(age=22, city='Muse', country='Myanmar')
print(message)

# Request input from console
input_message = input('Please enter your name : ')
print(input_message)