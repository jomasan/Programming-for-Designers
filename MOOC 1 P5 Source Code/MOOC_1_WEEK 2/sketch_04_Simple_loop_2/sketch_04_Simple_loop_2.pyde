"""_summary_
In this lesson, we draw primitives using a loop
    """

# Canvas dimensions
canvas_width = 1200  # Define the width of the canvas
canvas_height = 600  # Define the height of the canvas

def setup():
    # Create a canvas with the specified width and height. This function runs once at the start.
    size(canvas_width, canvas_height)

def draw():
    # Set the background color to black using the grayscale method. This function runs repeatedly to draw.
    background(0)
    
    for i in range(0, 20):
        # Calculate a blue color intensity based on the loop's iteration. This makes each rectangle's blue component unique.
        blue_color = (255/20.0) * i
        
        # Set the color used to fill shapes. The blue component varies, creating a gradient effect.
        fill(0, 200, blue_color)
        
        # Disable drawing the stroke (outline) of shapes for a cleaner look.
        noStroke()
        
        # Calculate the x-coordinate for the current rectangle to position them in a sequence across the canvas.
        x = (i * 30) + 100
        
        # Draw a rectangle at the calculated x-coordinate, 100 pixels from the top, with a width of 20 pixels and a height of 100 pixels.
        rect(x, 100, 20, 100)

        
        
