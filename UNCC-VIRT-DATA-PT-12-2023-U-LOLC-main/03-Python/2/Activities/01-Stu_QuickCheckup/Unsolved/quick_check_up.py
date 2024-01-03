# Incorporate random library
import random

# Print Hello User!
print("Hello User!")

# Take in User Input
userName = input("What is your name?")

# Respond Back with User Input

print(f"Hello {userName}!")

# Take in the User Favorite Number

userNum = int(input("What's your favorite number?"))

# Respond Back with a statement based on your favorite number

compNumber = 3

if userNum < compNumber:
    print("Your favorite number is lower than mine!")
elif userNum > compNumber:
    print("Your favorite number is higher than mine!")
elif userNum == compNumber:
    print("Your favorite number is the same as mine!")

    