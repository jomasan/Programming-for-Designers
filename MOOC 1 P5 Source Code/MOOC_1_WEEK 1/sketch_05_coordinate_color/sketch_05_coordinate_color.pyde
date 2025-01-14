
# Canvas dimensions
canvas_width = 1200
canvas_height = 600


def setup():
    # Create a canvas with the specifid width and height
    size(canvas_width, canvas_height)

    # Set background color to black using the grayscale mothod.
    background(0)

    # Set the stroke weight
    strokeWeight(5)

    # Set the stroke color to red
    stroke(255, 0, 0)
    # Draw a point
    point(100, 50)

    # Set the stroke color to green
    stroke(0, 255, 0)
    # Draw a point
    point(200, 250)

    # Set the stroke color to blue
    stroke(0, 0, 255)
    # Draw a point
    point(400, 150)
