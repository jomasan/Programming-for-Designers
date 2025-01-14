"""
Summary: This code uses the mouseX position to 
dynamically scale a cyan rectangle on the canvas, 
demonstrating the use of the map function to adjust 
scale based on user input.
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
    
    # Set the fill color to cyan with medium opacity and outline to white.
    fill(0,255,255, 150)
    stroke(255)
    
    # Save the current drawing context.
    pushMatrix()
    
    # Use the map function to scale the rectangle size based on the mouseX position.
    # mouseX is mapped from a range of 0 to canvas_width to a scale range of 1 to 2.
    scale_size = map(mouseX, 0, canvas_width, 1, 2.0)
    
    # Apply the calculated scale to the rectangle.
    scale(scale_size)
    rect(0, 0, 200, 200)
    
    # Restore the previous drawing context.
    popMatrix()
