"""
Summary: This code creates a 100x100 grid of rectangles 
that are individually rotated based on their grid position 
and the mouseX value, demonstrating complex transformations 
and interactions with user input.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)

def draw():
    # Clear the canvas with a black background each frame.
    background(0)
    
    # Iterate through a 100x100 grid.
    for i in range(0, 100):
        for j in range(0, 100):
            # Set the fill color to cyan with medium opacity and the stroke to white.
            fill(0,255,255, 150)
            stroke(255)
            
            # Calculate the position of each rectangle in the grid.
            x = i * 20
            y = j * 20
            # Save the current drawing context.
            pushMatrix()
            # Translate to the position of the rectangle.
            translate(x, y)
            # Calculate a rotation angle based on the grid positions.
            angle = radians(i * j)
            
            # Rotate the drawing context by an angle influenced by the mouseX position.
            rotate(angle * mouseX / 100)
            # Draw a rectangle at the translated and rotated origin.
            rect(0, 0, 20, 20)
            # Restore the previous drawing context.
            popMatrix()
