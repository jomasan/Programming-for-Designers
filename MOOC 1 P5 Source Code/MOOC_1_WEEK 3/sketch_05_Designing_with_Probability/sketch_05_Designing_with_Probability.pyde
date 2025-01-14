"""_summary_
Here we will start learning how we can use probability in design.
    """
import random  # Import the random module for generating random numbers.

# Canvas dimensions
canvas_width = 1200  # Set the width for the canvas.
canvas_height = 600  # Set the height for the canvas.

def setup():
    # Initialize the canvas with the specified width and height. This function runs once at the start.
    size(canvas_width, canvas_height)

    # Set the canvas background to black.
    background(0)
    # Disable the stroke for shapes to enhance the visual output.
    noStroke()
    
    # Nested loops to create a grid. The outer loop iterates over rows, and the inner loop iterates over columns.
    for i in range(0, 100):
        for j in range(0, 100):
            # Calculate the x and y coordinates based on the loop indices.
            x = i * 20
            y = j * 20
            
            # Generate a random number between 0 and 1.
            random_number = random.uniform(0, 1)
            
            # Check if the random number is greater than 0.05. This condition is true most of the time.
            if(random_number > 0.05):
                # Set the fill color to a random shade of blue.
                fill(0, 0, random.randrange(0, 255))
                # Draw a rectangle at the calculated coordinates with a fixed size of 15x15 pixels.
                rect(x, y, 15, 15)
            else:
                # If the random number is not greater than 0.05, set the fill color to red.
                fill(255, 0, 0)
                # Ensure the ellipse is drawn with its top-left corner at (x, y).
                ellipseMode(CORNER)
                # Draw an ellipse at the calculated coordinates with a fixed size of 15x15 pixels.
                ellipse(x, y, 15, 15)

            
            
    
   
        
    
