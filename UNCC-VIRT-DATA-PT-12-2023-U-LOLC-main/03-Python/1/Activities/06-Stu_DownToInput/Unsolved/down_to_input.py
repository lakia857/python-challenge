# Take input of you and your neighbor
me = input("What is your name?")
neighbor = input("What is your neighbor's name?")

# Take how long each of you have been coding
meMonths =int(input("How many months have you been coding?"))
neighborMonths = int(input("How many months has your neighbor been coding?e"))
# Add total month
totalMonths = meMonths + neighborMonths
# Print results
print(f"{me} and {neighbor} have been coding for {totalMonths} months combined.")
