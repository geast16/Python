first = input("Enter first number: ")
second = input("Enter second number: ")
print("Before swapping:", first, second)
first, second = second, first
print("After swapping:", first, second)


top_cities = [
    "New York City",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
]
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)
print(sorted(top_cities))
top_cities.sort()
print(top_cities)

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)
random_numbers.sort(reverse=True)
print(random_numbers)
