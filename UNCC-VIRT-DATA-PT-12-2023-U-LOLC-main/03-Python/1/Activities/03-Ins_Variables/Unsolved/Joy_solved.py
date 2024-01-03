# Create a variable called 'name' that holds a string
name = "Joy"
# Create a variable called 'country' that holds a string
country = "United States"
# Create a variable called 'age' that holds an integer
age = 50
# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 38
# Calculate the daily wage for the user
daily_wage = hourly_wage * 8
# Create a variable called 'satisfied' that holds a boolean
satisfied = True
# Print out "Hello <name>!"
print("Hello " + name + "!")  
# Print out what country the user entered
print(name + " lives in the " + country +".")
# Print out the user's age
print(name + " is " + str(age) + " yeas old." )
# With an f-string, print out the daily wage that was calculated
print(f"{name}'s daily wage is ${daily_wage}")
# With an f-string, print out whether the users were satisfied
print(f"Are you satisfied with your current wage? {satisfied}")