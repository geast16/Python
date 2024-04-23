def unique(lst=[]):
    """
    Function to remove duplicate elements from a list while preserving the original order.

    Args:
    lst (list): The input list containing any number of elements.

    Returns:
    list: A new list with all duplicate elements removed while preserving the original order.
    """
    unique_list = []  # Initialize an empty list to store unique elements

    # Iterate through the input list
    for item in lst:
        # If the item is not already in the unique_list, add it
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


# Example usage of the unique function
print(unique([1, 1, 4, 5, 1]))  # Output: [1, 4, 5]
print(unique(["Mark", "Mark", "John", "Anne"]))  # Output: ['Mark', 'John', 'Anne']
