"""
Summary: This code generates 1000 semi-transparent 
rectangles at random positions, demonstrating the use of 
pushMatrix() and popMatrix() for positioning.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the background color to black.
    background(0)
    # Set the fill color to cyan with low opacity for semi-transparent rectangles.
    fill(0,255,255,50)
    # Disable the stroke for a cleaner look.
    noStroke()
    
    # Generate and draw rectangles in random positions.
    for i in range(0, 1000):
        # Randomly determine the x and y positions for each rectangle.
        x = random.randrange(-100, canvas_width)
        y = random.randrange(-100, canvas_height)
        # Save the current drawing context.
        pushMatrix()
        # Translate the origin to the random x and y positions.
        translate(x, y)
        # Draw a rectangle at the translated origin.
        rect(0, 0, 30, 40)
        # Restore the previous drawing context.
        popMatrix()
