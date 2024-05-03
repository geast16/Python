numbers = [1, 2, 3, 4]
cells = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
print(cells[0])
print(cells[0][1])
print(cells[1][0])

for x in cells:
    print("Elements:", x)

table = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
for row in table:
    for cell in row:
        print("Element:", cell)

table = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
for row in table:
    for cell in row:
        print(cell, "", end="")
    print()

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

table = [[i for i in range(1, 6)] for rj in range(4)]
print(table)
