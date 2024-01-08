# x = 2


# if x < 2:
#     print("below 2")
# elif x >= 2:
#     print("Two or more")
# else:
#     print("something esle")

# hrs = input("Enter hours:")
# h = float(hrs)
# rate = input("Enter rate:")
# r = float(rate)

# if h <= 40:
#    print(r * h)
# elif h > 40:
#    print((40 * r) + (h -40) * (r *1.5))
   
score = (input("Enter Score:"))

try:
    score = float(score)

except:
    print("Choose score between 0.0 and 1.0")
if score > 1.0:
    print("Choose score between 0.0 and 1.0")

elif score >= 0.9:
    print("A")

elif score >= 0.8:
    print("B")
 
elif score >= 0.7:
    print("C")

elif score >= 0.6:
    print("D")

elif score < 0.6:
    print("F") 
    
