import random  # Import the random module

number = random.randint(0, 10)  # Generate a random number between 0 and 10 (inclusive)
threshold = 6  # Set the threshold value for comparison
threshold2 = 4  # Set another threshold value for comparison

if number < threshold:  # Check if the number is less than the threshold
    print("Small Number")  # Print "Small Number" if the condition is true
elif number > threshold:  # Check if the number is greater than the threshold
    print("Big Number")  # Print "Big Number" if the condition is true
else:  # If neither condition is true
    print("Number is", threshold)  # Print "Number is" followed by the threshold value

if number < threshold2:  # Check if the number is less than the second threshold
    print("Really Small Number")  # Print "Really Small Number" if the condition is true
print(number)  # Print the generated random number
