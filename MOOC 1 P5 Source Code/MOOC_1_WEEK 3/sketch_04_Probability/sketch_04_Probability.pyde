"""_summary_
This is an introduction to probability. 
Notice how we use if statements in conjunction with randomly generated values.
    """
import random  # Import the random module for generating random numbers.

# Canvas dimensions
canvas_width = 1200  # Set the width for the canvas.
canvas_height = 600  # Set the height for the canvas.

def setup():
    # Initialize the canvas with the specified width and height. This setup function runs once at the beginning.
    size(canvas_width, canvas_height)

    # Fill the background with black color to start.
    background(0)
    # Disable the stroke for the ellipses for a cleaner look.
    noStroke()
    
    # Loop 100 times to create 100 ellipses.
    for i in range(0, 100):
        # Generate a random x-coordinate within the canvas width.
        x = random.uniform(0, canvas_width)
        # Generate a random y-coordinate within the canvas height.
        y = random.uniform(0, canvas_height)
        
        # Generate a random number between 0 and 1 to decide the color of the ellipse.
        random_number = random.uniform(0, 1)
        # Print the generated random number to the console (mostly for debugging purposes).
        print(random_number)
        
        # Decide the fill color of the ellipse based on the random number.
        if(random_number > 0.2):
            # If the random number is greater than 0.2, set the ellipse color to red.
            fill(255, 0, 0)
        else:
            # If the random number is 0.2 or less, set the ellipse color to white.
            fill(255)
        
        # Draw the ellipse at the generated random position with a fixed size.
        ellipse(x, y, 20, 20)


    
   
        
    
