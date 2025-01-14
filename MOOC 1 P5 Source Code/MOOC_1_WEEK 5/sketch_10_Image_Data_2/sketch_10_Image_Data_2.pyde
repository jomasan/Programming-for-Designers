"""
Summary: This interactive sketch dynamically alters 
the pixels of a displayed portrait image based on 
mouse position, changing pixels to red if their 
brightness is below a threshold mapped from 
the mouse X coordinate, or white otherwise.
"""
import random

# Canvas dimensions
canvas_width = 500
canvas_height = 750

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the background color to black.
    background(0)
    
    # Load and display a portrait image onto the canvas.
    global img
    img = loadImage("portrait.jpg")
    image(img, 0, 0, 500, 750)
    
    # Prepare for pixel manipulation by loading the current canvas pixels.
    loadPixels()
    global total_pixels
    total_pixels = canvas_width * canvas_height

def draw():
    # Redisplay the image each frame for dynamic interaction.
    image(img, 0, 0, 500, 750)
    loadPixels()
    # Map the mouseX position to a brightness threshold.
    cut = map(mouseX, 0, canvas_width, 0, 255)
    
    # Iterate over all pixels in the image.
    for i in range(total_pixels):
        # Get the brightness of the current pixel.
        value = brightness(pixels[i])
        # Change the pixel color based on the brightness relative to the threshold.
        if value < cut:
            pixels[i] = color(255, 0, 0)  # Pixels darker than the threshold turn red.
        else:
            pixels[i] = color(255)  # Pixels lighter than the threshold turn white.
    
    # Apply the modified pixel colors to the canvas.
    updatePixels()
