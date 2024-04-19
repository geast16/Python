# Ask the user to guess the release year of Python 1.0
while True:
    guess = int(
        input("When was Python 1.0 released? ")
    )  # Add a space at the end of this prompt

    # Check if the guess is correct
    if guess == 1994:
        print("Correct!")
        break
    elif guess > 1994:
        print("It was earlier than that! ")  # Add a space at the end
    else:
        print("It was later than that! ")  # Add a space at the end
