

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
    background(0)

    # Set the stroke color to red
    stroke(255, 0, 0)

    # Draw a point where the cursor is
    point(mouseX, mouseY)

    # Call the display_cursor_coordinates() function to display the cursor coordinates on the canvas
    display_cursor_coordinates()


def display_cursor_coordinates():
    # Setting the text size
    textSize(14)
    # A string message with the x and y coordinates of the cursor
    cursor_coordinates = str(mouseX) + ", " + str(mouseY)
    # Displaying the text on the canvas using the x, y coordinates of the cursor
    text(cursor_coordinates, mouseX, mouseY)
