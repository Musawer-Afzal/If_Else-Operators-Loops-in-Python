lower_limit = int(input("Enter Lower Limit: "))
upper_limit = int(input("Enter Upper Limit: "))

for i in range(lower_limit, upper_limit + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)    