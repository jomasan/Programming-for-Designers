"""
Summary: This sketch, inspired by 'Kilo' by Light Light, 
features interactive cursor icons that change between 
two images based on randomness, against a retro-styled background.
"""
import random
# Canvas dimensions
canvas_width = 500
canvas_height = 750

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    
    # Load images for cursor icons and a retro background.
    global img, img2, img3
    img = loadImage("cursor_icon.png")
    img2 = loadImage("cursor_icon2.png")
    img3 = loadImage("retro.jpeg")
    # Display the background image to cover the entire canvas.
    image(img3, 0, 0, 500, 750)
    # Smooth edges of the shapes drawn.
    smooth()

def draw():
    # Change the cursor icon every 5 frames.
    if frameCount % 5 == 0:
        rand_number = random.uniform(0, 1.0)
        # Move the drawing position to follow the mouse cursor.
        translate(mouseX, mouseY)
        # Randomly choose between two cursor images, with one being less likely.
        if rand_number < 0.15:
            image(img2, 0, 0, 20, 20)
        else:
            image(img, 0, 0, 20, 20)
