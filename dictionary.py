var = {}  # Creating an empty dictionary

print(type(var))  # Printing the type of the variable 'var'

var2 = {
    "juice": "cranberry",
    "fruit": "mango",
}  # Creating a dictionary with key-value pairs

print(var2)  # Printing the content of 'var2'

print(
    var2["fruit"]
)  # Accessing and printing the value associated with the key 'fruit' in 'var2'

var2["food"] = "sandwich"  # Adding a new key-value pair to 'var2'

print(var2)  # Printing the modified 'var2'

del var2["juice"]  # Deleting the key-value pair with the key 'juice' from 'var2'

print(var2)  # Printing the modified 'var2'

var2["food"] = "pasta"  # Modifying the value associated with the key 'food' in 'var2'

print(var2)  # Printing the modified 'var2'

print(dir(var2))  # Printing the list of available methods and attributes for 'var2'

print(list(var2.keys()))  # Printing a list of keys in 'var2'

print(list(var2.values()))  # Printing a list of values in 'var2'

print(list(var2.items()))  # Printing a list of key-value pairs in 'var2'

for k, v in var2.items():  # Iterating through each key-value pair in 'var2'
    print(k, v)  # Printing each key-value pair

dict_of_lists = {
    "A": [0, 1, 2],
    "B": [2, 3, 4],
    "C": [4, 5, 6],
}  # Creating a dictionary of lists

for (
    k,
    v,
) in dict_of_lists.items():  # Iterating through each key-value pair in 'dict_of_lists'
    print(k, v)  # Printing each key-value pair
