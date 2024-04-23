numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# The option below is an example of list comprehensions
numbers = [i for i in range(1, 101)]
print(numbers)

# Imagine that we now want to generate numbers from 1 to 100 again, but we want to skip numbers that are divisible by three.
# Notice that 3, 6, 9, 12, 15, 18, 21, 24, 36, onward are no longer there
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)
