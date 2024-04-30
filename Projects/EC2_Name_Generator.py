import random
import string


# Function to generate a random string of letters and digits
def generate_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


# Function to generate unique EC2 names
def generate_ec2_names(num_instances, department):
    # Check if the department is valid
    valid_departments = ["Marketing", "Accounting", "FinOps"]
    if department not in valid_departments:
        print(
            "Invalid department. Please choose from Marketing, Accounting, or FinOps."
        )
        return

    # Generate unique names for the given number of instances
    ec2_names = []
    for i in range(1, num_instances + 1):
        ec2_name = f"{department}-Instance{i}-{generate_random_string()}"
        ec2_names.append(ec2_name)

    return ec2_names


# Main function
def main():
    # Input the number of EC2 instances and department name
    num_instances = int(input("Enter the number of EC2 instances: "))
    department = input("Enter your department (Marketing, Accounting, or FinOps): ")

    # Generate and print unique EC2 names
    ec2_names = generate_ec2_names(num_instances, department)
    if ec2_names:
        print("Unique EC2 Names:")
        for name in ec2_names:
            print(name)


if __name__ == "__main__":
    main()
