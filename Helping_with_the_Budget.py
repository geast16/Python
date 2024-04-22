spendings = [
    1346.0,
    987.50,
    1734.40,
    2567.0,
    3271.45,
    2500.0,
    2130.0,
    2510.30,
    2987.34,
    3120.50,
    4069.78,
    1000.0,
]

# Initialize counters for low, normal, and high spendings
low_count = 0
normal_count = 0
high_count = 0

# Go through the list of spendings and count the occurrences
for spending in spendings:
    if spending < 1000.0:
        low_count += 1
    elif 1000.0 <= spending <= 2500.0:
        normal_count += 1
    else:
        high_count += 1

# Print the results
print(
    "Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.".format(
        low_count, normal_count, high_count
    )
)
