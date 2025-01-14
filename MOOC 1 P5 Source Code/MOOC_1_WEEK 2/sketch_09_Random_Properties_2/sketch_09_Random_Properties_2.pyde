"""_summary_
In this lesson, we will learn about random numbers
    """
import random  # Import the random module for generating random numbers.

# Canvas dimensions
canvas_width = 1200  # Set the width for the canvas.
canvas_height = 600  # Set the height for the canvas.

def setup():
    # Initialize the canvas with the specified width and height. This setup runs once at the start.
    size(canvas_width, canvas_height)
    
    # Fill the canvas with a black background. This sets the base color for the drawing.
    background(0)
    
    # Set the fill color for the ellipses to white with low opacity (50 out of 255) for a subtle effect.
    fill(255, 50)
    # Disable the stroke (outline) of the ellipses for smoother visuals.
    noStroke()
    
    # Generate and draw 500 ellipses at random positions and sizes on the canvas.
    for i in range(0, 500):
        # Generate a random x-coordinate within the canvas width.
        x = random.randint(0, canvas_width)
        # Generate a random y-coordinate within the canvas height.
        y = random.randint(0, canvas_height)
        # Generate a random size for the ellipse between 1.0 and 100.0 pixels.
        rand_size = random.uniform(1.0, 100.0)
        
        # Draw an ellipse at the random coordinates with the random size.
        ellipse(x, y, rand_size, rand_size)

    
    
    
    
    
       
        
        
