# Ask the user for the number of hours worked and their hourly rate
hours_worked = float(
    input("How many hours did you work last month? ")
)  # Add a space at the end of this prompt
hourly_rate = float(
    input("What is your hourly rate? ")
)  # Add a space at the end of this prompt

# Calculate the salary
salary = hours_worked * hourly_rate

# Show the calculated salary
print(f"Last month, you earned {salary} dollars")
