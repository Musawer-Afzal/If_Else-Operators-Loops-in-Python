# Print 
# *
# **
# ***
# ...

rows = int(input("Enter the number of rows: "))

#for i in range(1, rows + 1):
#    # print("*" * i) for easy fix
#    for j in range(1, i + 1):
#        print("*", end = " ")
#    print()    # To move code to new line    


for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    for k in range(i - 1, 0, -1):
        print(k, end = " ")
    print()