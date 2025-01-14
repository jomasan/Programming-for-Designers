"""_summary_
In this lesson, we will create a composition using nested loops
    """
import random  # Import the random module for generating random numbers.

# Canvas dimensions
canvas_width = 1200  # Define the width of the canvas.
canvas_height = 600  # Define the height of the canvas.

def setup():
    # Initialize the canvas with the specified width and height. This setup function runs once at the beginning.
    size(canvas_width, canvas_height)
    
    # Fill the canvas with a black background. This sets the initial state for the drawing.
    background(0)
    # Set the blend mode to ADD which makes overlapping areas brighter.
    blendMode(ADD)
    # Disable the stroke (outline) for the rectangles to focus on the fill color.
    noStroke()
    
    # Create a grid of rectangles with randomized positions and sizes using nested loops.
    for i in range(0, 61):  # Horizontal loop for column placement.
        for j in range(0, 31):  # Vertical loop for row placement.
            
            # Calculate the x position with an added random offset to vary the placement.
            x = (i * 20) + random.uniform(1, 20.0)
            # Calculate the y position based on the row number.
            y = j * 20
            # Randomize the width of the rectangle between 10 and 50 pixels.
            x_size = random.uniform(10, 50.0)
            
            # Generate a random value for the blue component of the RGBA color.
            random_blue = random.randrange(0, 255)
            
            # Set the fill color to a semi-transparent shade of blue.
            fill(0, 255, random_blue, 150)
            
            # Draw the rectangle with randomized positioning and size.
            rect(x, y, x_size, 18)

    

    
    
    
    
       
        
        
