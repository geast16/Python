import random

number = random.randint(0, 10)
if number < 7:
    print("Small Number")
elif number > 7:
    print("Big Number")
else:  # elif number == 7:
    print("Number is 7")
print(number)
