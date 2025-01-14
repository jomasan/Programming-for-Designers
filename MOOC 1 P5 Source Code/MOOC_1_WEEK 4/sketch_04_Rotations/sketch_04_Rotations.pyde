"""
Summary: This code dynamically rotates a rectangle 
around the canvas origin based on the mouseX position, 
illustrating the use of rotation and matrix push/pop 
in an animated sketch.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    
def draw():
    # Set the background color to black on each frame for a clean slate.
    background(0)
    
    # Set the fill color to cyan with medium opacity and outline to white.
    fill(0,255,255, 150)
    stroke(255)
    
    # Save the current drawing context.
    pushMatrix()

    # Calculate the rotation angle based on the mouseX position.
    angle = radians(mouseX)
    
    # Rotate the drawing context by the calculated angle.
    rotate(angle)
    # Draw a rectangle. Its rotation center is the canvas origin (0,0).
    rect(0, 0, 200, 200)
    
    # Restore the previous drawing context.
    popMatrix()
