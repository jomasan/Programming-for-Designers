"""_summary_
In this lesson, we draw four idential rectangles on the Canvas.
    """

# Canvas dimensions
canvas_width = 1200
canvas_height = 600


def setup():
    # Create a canvas with the specifid width and height
    size(canvas_width, canvas_height)

    # Set the stroke weight
    strokeWeight(5)


def draw():
    # Set background color to black using the grayscale mothod.
    background(255,0,120)

    # Set stroke color to white using the grayscale mothod.
    stroke(0,0,120)

    # Set the fill color to cyan using RGB method.
    fill(0, 120, 230)

    # Draw a rectangle (starting from the top left corner)
    rect(100, 100, 300, 300)
    
    # Draw an ellipse (starting from the center)
    ellipse(500,200,200,200)
