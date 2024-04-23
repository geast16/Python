# Given list of flight connections
connections = [
    ("Amsterdam", "Dublin", 100),
    ("Amsterdam", "Rome", 140),
    ("Warsaw", "Rome", 130),
    ("Minsk", "Prague", 95),
    ("Stockholm", "Rome", 190),
    ("Copenhagen", "Paris", 120),
    ("Madrid", "Rome", 135),
    ("Lisbon", "Rome", 170),
    ("Dublin", "Rome", 170),
]

# Initialize variables to count connections to Rome and total flight time
connections_to_rome = 0
total_flight_time = 0

# Iterate through the connections
for connection in connections:
    # Check if the destination is Rome
    if connection[1] == "Rome":
        connections_to_rome += 1
        total_flight_time += connection[2]

# Calculate the average flight time
average_flight_time = total_flight_time / connections_to_rome

# Print the output
print(
    "{} connections lead to Rome with an average flight time of {} minutes".format(
        connections_to_rome, average_flight_time
    )
)
