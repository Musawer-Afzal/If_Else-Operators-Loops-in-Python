# Operators

# 1. Arithmetic Operators
print(5+6)
print(5-6)
print(5*6)
print(5/6)
# Power of eg. 5^6
print(5**6)
print(5%6)
# Floor Division(Integer Division): Convert the result into integer
print(5//6)


# 2. Comparison Operators
# Equal to
print(5==5)
# Not Equal to
print(5!=5)
# Greater than
print(5>5)
# Less than
print(5<5)
# Greater than or Equal to
print(5>=5)
# Less than or Equal to
print(5<=5)


# 3. Logical Operators
# And
print(1 and 0)
# Or
print(1 or 0)
# Not
print(not 0)


# 4. Bitwise Operators
# Bitwise AND
print(5 & 6)
# Bitwise OR
print(5 | 6)
# Bitwise NOT
print(~5)
# Bitwise XOR
print(5 ^ 6)
# Left Shift
print(5 << 2)
# Right Shift
print(5 >> 2)


# 5. Assignment Operators
# Simple Assignment
x = 5
# Compound Assignment
x += 5
# Multiple Assignment
a, b = 1, 2
# Multiple Assignment   
a, b = b, a + b


# 6. Membership Operators
# In
print(5 in [1, 2, 3, 4, 5])
# Not In
print(5 not in [1, 2, 3, 4, 5])


# For Loop      
for i in range(1,    11):
    print(i) # start  end 11-1. answer 1,2,3,4,5,6,7,8,9,10

for i in range(1, 11, 2):
    print(i) # start  end 11-1. answer 1,3,5,7,9  


# Nested Loops
for i in range(1, 5):
    for j in range(1, 5):
        print(i,j)


# Break Statement
for i in range(1, 11):
    if i == 5:
        break
    print(i) # start  end 11-1. answer 1,2,3,4


# Continue Statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i) # start  end 11-1. answer 1,2,3,4,6,7,8,9,10


# Pass Statement: Used to pass a code without doing anything
# Example, To not allow thr compiler to throw an error but include code in program
for i in range(1, 11):
        pass