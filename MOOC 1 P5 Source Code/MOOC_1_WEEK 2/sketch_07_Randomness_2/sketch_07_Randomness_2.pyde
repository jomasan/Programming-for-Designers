"""_summary_
In this lesson, we will learn about random numbers
    """
import random  # Import the random module to use its functions for generating random numbers.

# Canvas dimensions
canvas_width = 1200  # Set the width of the canvas
canvas_height = 600  # Set the height of the canvas

def setup():
    # Initialize the canvas with the specified width and height. This setup function runs once.
    size(canvas_width, canvas_height)
    
    # Demonstrates generating a sequence of random integers using the randint function.
    print("Sequence 1")
    for i in range(0, 5):
        # Generate a random integer between 0 and 1, inclusive, and print it.
        random_int_number = random.randint(0, 1)  # Both start and end values are included.
        print(random_int_number)
    
    # Demonstrates generating a sequence of random numbers using the randrange function.
    print("Sequence 2")
    for i in range(0, 5):
        # Generate a random integer between 0 and up to (but not including) 1, and print it.
        random_number = random.randrange(0, 1)  # End value is excluded.
        print(random_number)

def draw():
    # Fill the canvas with a black background. This draw function can be executed repeatedly.
    background(0)

    
    
       
        
        
