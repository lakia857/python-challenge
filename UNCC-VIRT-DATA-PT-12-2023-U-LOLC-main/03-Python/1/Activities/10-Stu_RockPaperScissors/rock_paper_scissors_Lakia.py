# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

print(f"You chose {user_choice}. Computer chose {computer_choice}")

# Run Conditionals
if user_choice == "r" and computer_choice == "r":
    print("The game is tied")
elif user_choice == "r" and computer_choice == "p":
    print("Computer wins the game")
elif user_choice == "r" and computer_choice == "s":
    print("User wins the game")
elif user_choice == "p" and computer_choice == "r":
    print("User wins the game")
elif user_choice == "p" and computer_choice == "p":
    print("The game is tied")
elif user_choice == "p" and computer_choice == "s":
    print("Computer wins the game")
elif user_choice == "s" and computer_choice == "r":
    print("Computer wins the game")
elif user_choice == "s" and computer_choice == "p":
    print("User wins the game")
else:
    print("The game is tied")

