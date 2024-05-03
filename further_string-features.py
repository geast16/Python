fav_rapper = "Lupe Fiasco"
print(fav_rapper[5])
print(fav_rapper[:5])
print(fav_rapper[5:])

text = "please capatilze me"
text_cap = text.upper()
print(text_cap)

user_number = input("Please provide a number: ")
if user_number.isnumeric():
    print("Thank you, that's a correct number!")
else:
    print("Sorry,", user_number, "is not a number!")
