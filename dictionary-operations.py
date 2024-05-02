grades = {}
grades["John"] = "A-"
grades["Ann"] = "B+"
print(grades)

grades["Ann"] = "A-"
print(grades)

grades.update({"John": "A"})
print(grades)

print(len(grades))

if "John" in grades:
    print("John got a(n):", grades["John"])

# del grades["Ann"]
# print(grades)

for grade in grades:
    print(grade)

for grade in grades.values():
    print(grade)

for person, grade in grades.items():
    print(person, "got an", grade)
