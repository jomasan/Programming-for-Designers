"""_summary_
Here we will learn how to perform loops using a while statement.
    """
import random  # Import the random module for generating random numbers.

# Canvas dimensions
canvas_width = 1200  # Set the width of the canvas.
canvas_height = 600  # Set the height of the canvas.

def setup():
    # Initialize the canvas with the specified width and height. This setup function runs once at the beginning.
    size(canvas_width, canvas_height)

    # Fill the background with black color.
    background(0)
    # Set the stroke weight to 1 for any shapes that might use strokes.
    strokeWeight(1)
    # Initialize variable x with a large value for the diameter of the first ellipse.
    x = 3000
    
    # Use a while loop to draw ellipses with decreasing sizes.
    while x > 5:
        # Set the ellipse mode to CENTER, meaning the x and y parameters will specify the center of the ellipse.
        ellipseMode(CENTER)
        # Set the fill color of the ellipse to a random RGB color.
        fill(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        # Disable the stroke for the ellipses.
        noStroke()
        # Draw an ellipse at the center of the canvas with the current value of x for both width and height.
        ellipse(600, 300, x, x)
        # Decrease the value of x by a random amount between 1 and 20, creating ellipses with progressively smaller sizes.
        x -= random.randrange(1, 20)



    
   
        
    
