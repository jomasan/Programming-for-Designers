"""_summary_
This is a lesson on Conditional Statements. We will learn the use of if and else.
    """

# Canvas dimensions
canvas_width = 1200  # Set the width for the canvas.
canvas_height = 600  # Set the height for the canvas.

x = 0  # Initialize a global variable x to 0. This will determine the x-coordinate of the ellipse.

def setup():
    # Initialize the canvas with the specified width and height. This setup function runs once at the beginning.
    size(canvas_width, canvas_height)

def draw():
    # Declare x as global to modify its value within this function.
    global x
    
    # Fill the canvas with a black background. This effectively clears the canvas in each frame.
    background(0)
    
    # Increment x to move the ellipse horizontally across the canvas.
    x += 1
    
    # Disable the stroke (outline) of the ellipse for a cleaner look.
    noStroke()
    
    # Use an if statement to change the color of the ellipse based on its x-coordinate.
    if x > 200:
        # Change the ellipse's fill color to red if x is greater than 200.
        fill(255, 0, 0)
    else:
        # Keep the ellipse's fill color white if x is less than or equal to 200.
        fill(255)
    
    # Draw the ellipse at the moving x-coordinate, 300 pixels down from the top, with a width and height of 50 pixels.
    ellipse(x, 300, 50, 50)
    
    # Optionally, draw a vertical line at x=200 to visualize the threshold for the color change.
    stroke(255)  # Set the line color to white.
    line(200, 0, 200, canvas_height)  # Draw the line from the top to the bottom of the canvas.
