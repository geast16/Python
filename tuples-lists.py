city_1 = ("London", "UK", 8.98)
city_2 = ("Denver", "Colorado", 0.6)
city_3 = ("Rio de Janero", "Brasil", 4.5)

captials = [
    ("London", "UK", 8.98),
    ("Denver", "Colorado", 0.6),
    ("Rio de Janero", "Brasil", 4.5),
]

for capital in captials:
    print("Name:", capital[0], ", Country:", capital[1], ", Population:", capital[2])

user_data = ("John", "American", 1994, [77.0, 78.2, 77.5])
user_data[3].append(79.6)
print(user_data)
