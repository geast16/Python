# Ask the user three questions
days_ago = int(
    input("How many days ago have you purchased the item? ")
)  # Add a space at the end of this prompt
used_item = input(
    "Have you used the item at all [y/n]? "
)  # Add a space at the end of this prompt
broken_down = input(
    "Has the item broken down on its own [y/n]? "
)  # Add a space at the end of this prompt

# Check if the user can get a refund based on the refund policy
if (days_ago <= 10 and used_item == "n") or broken_down == "y":
    print("You can get a refund.")
else:
    print("You cannot get a refund.")
