def split_and_join(line):
    # Split the string on space delimiter
    words = line.split(" ")

    # Join the words using hyphen
    joined_line = "-".join(words)

    return joined_line


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
