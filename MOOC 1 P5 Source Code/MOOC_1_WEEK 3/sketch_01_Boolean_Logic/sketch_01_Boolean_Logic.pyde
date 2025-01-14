"""_summary_
Introduction to Boolean operators
    """

# Canvas dimensions
canvas_width = 1200  # Define the width of the canvas.
canvas_height = 600  # Define the height of the canvas.

def setup():
    # Initialize the canvas with the specified width and height. This setup runs once at the beginning.
    size(canvas_width, canvas_height)

    # Initialize variables a and b with values 5 and 10, respectively.
    a = 5
    b = 10
    
    # Perform various comparisons between a and b using Boolean operators and print the results.
    
    # Check if a is greater than b and print the result.
    print(a > b)  # This will print False because 5 is not greater than 10.
    
    # Check if a is less than b and print the result.
    print(a < b)  # This will print True because 5 is less than 10.
    
    # Check if a is equal to b and print the result.
    print(a == b)  # This will print False because 5 is not equal to 10.
    
    # Check if a is less than or equal to b and print the result.
    print(a <= b)  # This will print True because 5 is less than 10.
    
    # Check if a is greater than or equal to b and print the result.
    print(a >= b)  # This will print False because 5 is not greater than or equal to 10.
    
    # Check if a is not equal to b and print the result.
    print(a != b)  # This will print True because 5 is not equal to 10.
