# The currnt population of a town is 10000. The Population of the town is increasing at the rate of 10% per year.
# You have to write a program to find out the population at the end of each year of the last 10 years

curr_pop = 10000    
curr_year = 2024

for i in range(10, 0, -1):
    curr_year  = curr_year - 1 

    # We need to find the 10% of 9000, mean previous year
    # population in 9th year = x
    # x + 10% of x = 10000
    # x + 0.1 of x = 10000
    # 1.1 of x = 10000
    # x = 10000 / 1.1
    print("Population in Year", curr_year, ": ", curr_pop)
    curr_pop = curr_pop / 1.1