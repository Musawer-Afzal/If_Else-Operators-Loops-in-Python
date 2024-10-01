a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))

if a < b and a < c:
    print("Smallest number is: ", a)
elif b < c and b < a:
    print("Smallest number is: ", b)
else:
    print("Smallest number is: ", c)    