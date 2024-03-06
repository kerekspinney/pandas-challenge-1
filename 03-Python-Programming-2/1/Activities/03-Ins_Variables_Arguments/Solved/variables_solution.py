"""Passing Arguments."""

test = 1


# Define a function that will add two numbers.
def add():
    """This function takes two numbers and adds them and then returns the total."""
    first_number = 1 # This is a local scope of the function.
    second_number = 2 # This is a local scope of the function.
    total = first_number + second_number
    print(f"Your total is: {total}")
    print(test)


# if __name__ == "__main__":
#     add()
    # print(first_number)


# Global variables for first_number and second_number.
first_number = 2
second_number = 3

# Define a function that will add two numbers.
def addition():
    """This function takes two numbers and adds them and then returns the total."""
    first_number = 1 # This is a local variable of the function.
    second_number = 2 # This is a local variable of the function.
    total = first_number + second_number
    print(f"Your total is: {total}")

print("Total", first_number + second_number )

if __name__ == "__main__":
    addition()
    print(f"The global variables for the 'first_number' and 'second_number` are {first_number} and {second_number}")
