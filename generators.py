def get_number():
    for i in range(1, 5):  # second index means it will stop at the prior number, 4
        yield i


generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))  # index 4

for x in get_number():
    print(x)

numbers = list(get_number())
print(numbers)
