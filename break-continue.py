while True:
    name = input("Enter your name or EXIT to close the program: ")
    if name == "EXIT":
        break
    print("Hello", name)

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
