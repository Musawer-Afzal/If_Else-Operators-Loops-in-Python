fnum = int(input("Enter first number: "))
snum = int(input("Enter second number: "))

print("Enter which operation would you like to perform? ")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")

choice = input("Enter choice (a/ b/ c/ d): ")

if choice == "a":
    print(fnum, " + ", snum, "=", fnum + snum)
elif choice == "b":
    print(fnum, " - ", snum, "=", fnum - snum)
elif choice == "c":
    print(fnum, " * ", snum, "=", fnum * snum)
elif choice == "d":
    print(fnum, " / ", snum, "=", fnum / snum)
else:
    print("Invalid input")