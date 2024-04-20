import random  # Import the random module

number = random.randint(0, 10)  # Generate a random number between 0 and 10 (inclusive)
counter = 0  # Initialize a counter variable to count the number of iterations

# Start a while loop that continues until the generated number is 7 or the counter reaches 13
while number != 7:
    number = random.randint(0, 10)  # Generate a new random number
    counter = counter + 1  # Increment the counter by 1 for each iteration
    # Check if the counter reaches 13
    if counter >= 13:
        break  # Exit the loop if the counter reaches 13

print(counter, number)  # Print the counter value and the final generated number

# Start a for loop that iterates over the numbers from 0 to 9
for i in range(10):
    # Check if the square of the current number is less than 50
    if i**2 < 50:
        print(i, i**2)  # Print the current number and its square
    else:
        break  # Exit the loop if the square of the current number exceeds 50

print(i)  # Print the value of i after the loop terminates
