"""_summary_
In this lesson, we will learn about random numbers
    """
# Import the random module to access its functions for generating random numbers.
import random

# Canvas dimensions
canvas_width = 1200  # Define the width of the canvas
canvas_height = 600  # Define the height of the canvas

def setup():
    # Create a canvas with the specified width and height. This function runs once at the start.
    size(canvas_width, canvas_height)
    
    # Demonstrate accessing the random number function within a loop.
    for i in range(0, 5):
        # Generate a random float number between 0.0 and 1.0, and assign it to 'random_number'.
        random_number = random.random()
        # Print the generated random number to the console.
        print(random_number)

def draw():
    # Set the background color to black using the grayscale method. This function can run repeatedly to draw.
    background(0)

    
    
       
        
        
