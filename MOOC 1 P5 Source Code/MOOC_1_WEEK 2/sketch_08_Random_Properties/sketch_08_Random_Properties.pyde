"""_summary_
In this lesson, we will learn about random numbers
    """
import random  # Import the random module to generate random numbers.

# Canvas dimensions
canvas_width = 1200  # Define the width of the canvas.
canvas_height = 600  # Define the height of the canvas.

def setup():
    # Initialize the canvas with the specified width and height. This function runs once.
    size(canvas_width, canvas_height)
    
    # Fill the canvas with a black background. This sets the initial canvas state.
    background(0)
    
    # Set the fill color to white with low opacity (50 out of 255) for drawing ellipses.
    fill(255, 50)
    # Disable drawing the stroke (outline) for the ellipses for a cleaner look.
    noStroke()
    
    # Generate and draw 5000 ellipses at random positions on the canvas.
    for i in range(0, 5000):
        # Generate a random x-coordinate within the canvas width.
        x = random.randint(0, canvas_width)
        # Generate a random y-coordinate within the canvas height.
        y = random.randint(0, canvas_height)
        # Draw an ellipse at the random coordinates with a width and height of 20 pixels.
        ellipse(x, y, 20, 20)

    

    
    
    
    
       
        
        
