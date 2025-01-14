# Functions

# Define a function named 'print_sum' that takes two parameters: x and y.
# This function will calculate the sum of x and y, and print the inputs and the result.
def print_sum(x, y):
    # Print the first input with a message.
    print("input 1: " + str(x))
    
    # Print the second input with a message.
    print("input 2: " + str(y))
    
    # Calculate the sum of x and y, and store it in a variable named 'sum'.
    sum = x + y
    
    # Print the result of adding x and y with a message.
    print("Result: " + str(sum))

# Call the function 'print_sum' with 2 and 3 as arguments.
# This will execute the function with x=2 and y=3, and print their inputs and the result of their sum.
print_sum(2, 3)
