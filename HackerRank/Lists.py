# Initialize an empty list
lst = []

# Read input for the number of commands
N = int(input())

# Iterate through each command
for _ in range(N):
    # Read the command and split it into parts
    command = input().split()

    # Execute the command based on its type
    if command[0] == "insert":
        # Insert the element at the specified position
        lst.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        # Print the list
        print(lst)
    elif command[0] == "remove":
        # Remove the first occurrence of the specified element
        lst.remove(int(command[1]))
    elif command[0] == "append":
        # Append the element to the end of the list
        lst.append(int(command[1]))
    elif command[0] == "sort":
        # Sort the list
        lst.sort()
    elif command[0] == "pop":
        # Pop the last element from the list
        lst.pop()
    elif command[0] == "reverse":
        # Reverse the list
        lst.reverse()
