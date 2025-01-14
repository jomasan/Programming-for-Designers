"""
Summary: Enhanced sketch inspired by 'Kilo' by Light Light, 
featuring cursor icon changes and the ability to 
save individual frames or record a sequence of frames 
with toggleable recording via 'r' or 'R' keypress, 
set against a retro background.
"""
import random
# Canvas dimensions
canvas_width = 500
canvas_height = 750

# Flag to control frame recording
recording = False

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    
    # Load cursor icons and a retro background image.
    global img, img2, img3
    img = loadImage("cursor_icon.png")
    img2 = loadImage("cursor_icon2.png")
    img3 = loadImage("retro.jpeg")
    # Display the background image across the entire canvas.
    image(img3, 0, 0, 500, 750)
    # Enable smoothing for better visual quality.
    smooth()

def draw():
    global recording
    # Change the cursor icon every 5 frames based on randomness.
    if frameCount % 5 == 0:
        rand_number = random.uniform(0, 1.0)
        # Move the drawing position to the cursor location.
        translate(mouseX, mouseY)
        # Display one of two cursor images, with one being less frequent.
        if rand_number < 0.15:
            image(img2, 0, 0, 20, 20)
        else:
            image(img, 0, 0, 20, 20)
    
    # If recording is enabled, save each frame to a file.
    if recording:
        saveFrame("anim/frame-######.png")

def keyPressed():
    global recording
    # Save the current canvas as an image when 's' or 'S' is pressed.
    if key == 's' or key == 'S':
        saveFrame("images/img-######.png")
        print("Image saved")
    # Toggle recording on or off when 'r' or 'R' is pressed.
    if key == 'r' or key == 'R':
        recording = not recording
        print("Recording toggled.")
