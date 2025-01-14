"""_summary_
In this lesson, we will learn how to construct a grid using nested loops
    """
import random  # Although the random module is imported, it's not used in this snippet.

# Canvas dimensions
canvas_width = 1200  # Define the width of the canvas.
canvas_height = 600  # Define the height of the canvas.

def setup():
    # Initialize the canvas with the specified width and height. This setup runs once at the beginning.
    size(canvas_width, canvas_height)
    
    # Fill the canvas with a black background. This sets the initial state for the drawing.
    background(0)
    
    # Set the fill color for the circles to white with low opacity (50 out of 255).
    fill(255, 50)
    # Disable the stroke (outline) for the circles to enhance the visual effect.
    noStroke()
    
    # Create a grid of circles using nested loops.
    for i in range(0, 61):  # Horizontal loop, determines the x position.
        for j in range(0, 31):  # Vertical loop, determines the y position.
            
            # Calculate the x position based on the iteration variable and spacing.
            x = i * 20
            # Calculate the y position based on the iteration variable and spacing.
            y = j * 20
        
            # Draw a circle at the calculated position with a fixed diameter of 20 pixels.
            ellipse(x, y, 20, 20)

    

    
    
    
    
       
        
        
