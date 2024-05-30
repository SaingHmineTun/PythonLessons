# There are 2 types of loop
# 1. while loop
index = 5
while index < 100:
    index += 1
    if index % 2 == 1:
        continue
    
    print("Hello", index)
    
    if index == 20:
        break
    
# 2. for loop using range
for i in range(5, 20, 2):
    print("For Loop", i)
    

# For loop with list or string
name = "Sai Saing Hmine Tun"
for i in name:
    print(i, end="")
else:
    # execute at the end of loop
    print('\n#####################')
    

x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    
    
print(x)