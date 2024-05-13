import os

def get_file_info(path='.'):
    """
    Function to get information about files in a directory.

    Args:
    path (str, optional): Path to the directory to search for files. Defaults to '.' (current directory).

    Returns:
    list: List of dictionaries containing file information.
    """
    file_list = []  # List to store file information dictionaries
    for root, dirs, files in os.walk(path):  # Walk through the directory tree
        for file_name in files:  # Iterate through files in each directory
            file_path = os.path.join(root, file_name)  # Get the full path of the file
            file_size = os.path.getsize(file_path)  # Get the size of the file
            # Create a dictionary with file name and size and add it to the list
            file_info = {'name': file_name, 'size': file_size}
            file_list.append(file_info)
    return file_list  # Return the list of file information dictionaries

if __name__ == "__main__":
    # If the script is executed directly, get file information from the current directory
    file_info_list = get_file_info()
    print(file_info_list)  # Print the list of file information dictionaries
