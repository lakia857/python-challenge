# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

numstochose = int(input('How many numbers would you like to enter?'))
numbers = []
for i in range(numstochose):
    numbers.append(int(input('Next number: ')))
# Test your function with the following:
print(average(numbers))
#print(average(range(11)))
print(range(11))
x = 2
print (x)
