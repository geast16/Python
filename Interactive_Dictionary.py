# Interactive_Dictionary

# Sample dictionary containing English and German words
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase",
}

# Prompt the user to enter a word in English or EXIT
print("Enter a word in English or EXIT: ", end="")

# Infinite loop to keep asking the user for words until EXIT is entered
while True:
    # Accept user input
    word = input().strip().lower()

    # Check if the user wants to exit the program
    if word == "exit":
        print("Bye!")
        break  # Exit the loop and terminate the program

    # Check if the entered word exists in the dictionary
    if word in sample_dict:
        print("Translation: {}".format(sample_dict[word]))
    else:
        print("No match!")  # Print "No match!" if the word is not in the dictionary

    # Prompt the user to enter a word in English or EXIT for the next iteration
    print("Enter a word in English or EXIT: ", end="")
