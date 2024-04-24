var = []  # Creating an empty list

print(type(var))  # Printing the type of the variable 'var'

var2 = [151, 251, 386, 493, 649, "009"]  # Creating a list with mixed data types

print(var2)  # Printing the content of 'var2'

var2.append(721)  # Appending an element to 'var2' in place

print(var2)  # Printing the modified 'var2'

var2 = var2 + [445]  # Adding an element to 'var2' without modifying it in place

print(var2)  # Printing the modified 'var2'

numbers = [1, 2, 3, 4, 5]  # Creating a list of numbers

for number in numbers:  # Iterating through each element in 'numbers'
    print(number)  # Printing each number

numbers2 = list(range(0, 50))  # Creating a list of numbers using range()

print(numbers2)  # Printing the list 'numbers2'

for number in numbers2:  # Iterating through each element in 'numbers2'
    print(number)  # Printing each number

for i in range(10):  # Iterating through a range of numbers from 0 to 9
    print(i * 2)  # Printing the double of each number

print(numbers[2])  # Accessing and printing the element at index 2 in 'numbers'

print(len(numbers))  # Printing the length of the list 'numbers'

list_of_lists = [[0, 1, 2], [2, 3, 4], [4, 5, 6]]  # Creating a list of lists

print(list_of_lists)  # Printing the list of lists 'list_of_lists'

for list_of_list in list_of_lists:  # Iterating through each sublist in 'list_of_lists'
    for element in list_of_list:  # Iterating through each element in the sublist
        print(element)  # Printing each element
