"""
Summary: This interactive sketch, inspired by 'Kilo' by Light Light, 
alternates between two cursor images on a retro background, 
with added functionality to save the frame as an image when 's' or 'S' is pressed.
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
    # Apply smoothing to the drawing.
    smooth()

def draw():
    # Update the cursor icon every 5 frames based on a random chance.
    if frameCount % 5 == 0:
        rand_number = random.uniform(0, 1.0)
        # Move the drawing position to follow the mouse cursor.
        translate(mouseX, mouseY)
        # Randomly select one of two cursor images to display, with one being less frequent.
        if rand_number < 0.15:
            image(img2, 0, 0, 20, 20)
        else:
            image(img, 0, 0, 20, 20)

def keyPressed():
    # Save the current canvas as an image when 's' or 'S' is pressed.
    if key == 's' or key == 'S':
        saveFrame("images/img-######.png")
        print("Image saved")
