"""_summary_
In this lesson, we primitives using a loop
    """

# Canvas dimensions
canvas_width = 1200  # Set the canvas width
canvas_height = 600  # Set the canvas height

def setup():
    # Create a canvas with the specified width and height
    size(canvas_width, canvas_height)

def draw():
    # Set the background color to black using the grayscale method.
    background(0)
    
    for i in range(0, 20):
        # Set the color used to fill shapes - in this case, a shade of blue.
        fill(0, 200, 255)
        # Disable drawing the stroke (outline) of shapes.
        noStroke()
        
        # Calculate the x-coordinate for the current rectangle. This creates a horizontal sequence of rectangles.
        x = (i * 30) + 100
        
        # Draw a rectangle at the calculated x-coordinate, 100 pixels from the top of the canvas,
        # with a width of 20 pixels and a height of 100 pixels.
        rect(x, 100, 20, 100)


        
        
        
        
        
