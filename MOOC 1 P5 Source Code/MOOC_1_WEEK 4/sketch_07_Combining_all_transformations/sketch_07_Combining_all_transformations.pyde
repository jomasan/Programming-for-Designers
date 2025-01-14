"""
Summary: This code creates a dynamic grid of rectangles 
that scale and rotate based on mouse position, 
showcasing the combined use of map, rotate, 
and scale functions for interactive visual effects.
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
    
    # Iterate over a 100x100 grid to draw rectangles.
    for i in range(0, 100):
        for j in range(0, 100):
            # Set the fill color to cyan with medium opacity and outline to white.
            fill(0,255,255, 150)
            stroke(255)
            
            # Calculate the position for each rectangle.
            x = i * 20
            y = j * 20
            # Save the current drawing context.
            pushMatrix()
            # Translate to the position of each rectangle.
            translate(x, y)
            
            # Use the map function to adjust the scale factor based on mouseX position.
            scale_size_mult = map(mouseX, 0, canvas_width, 0.2, 1)
            # Use the map function to adjust the rotation factor based on mouseY position.
            rotation_mult = map(mouseY, 0, canvas_height, 0, 1)
            
            # Calculate an angle for rotation based on grid position.
            angle = radians(i * j)
            # Calculate a scale size based on grid position, with the domain remapped.
            scale_size = map(i * j, 0, 10000, 0.1, 10)
            
            # Apply rotation and scale based on the calculated factors and mouse position.
            rotate(angle * rotation_mult)
            scale(scale_size * scale_size_mult)
            # Draw a rectangle at the transformed position.
            rect(0, 0, 20, 20)
            
            # Restore the previous drawing context.
            popMatrix()
