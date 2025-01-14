"""
Summary: This code demonstrates loading and displaying 
an image in three different ways: 
normally, rotated, and both scaled and rotated, 
to illustrate image manipulation techniques in Processing.
"""
# Canvas dimensions
canvas_width = 1200
canvas_height = 600

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    
    # Load an image named 'gradient.png' into the program.
    global img
    img = loadImage("gradient.png")
    # Set the background color to black.
    background(0)

def draw():
    # Move the origin to a slight offset from the top-left corner.
    translate(20, 20)
    # Display the image in its original form.
    image(img, 0, 0, 200, 200)
    
    # Move the origin to the right, preparing for the rotated image.
    translate(400, 0)
    # Rotate the drawing context by 45 degrees (PI/4 radians).
    rotate(PI / 4)
    # Display the same image, now rotated.
    image(img, 0, 0, 200, 200)
    
    # Move the origin further to the right, preparing for the scaled and rotated image.
    translate(400, 0)
    # Apply an additional rotation of 45 degrees on top of the existing rotation.
    rotate(PI / 4)
    # Scale the drawing context to half size.
    scale(0.5)
    # Display the image again, now both scaled and rotated.
    image(img, 0, 0, 200, 200)
