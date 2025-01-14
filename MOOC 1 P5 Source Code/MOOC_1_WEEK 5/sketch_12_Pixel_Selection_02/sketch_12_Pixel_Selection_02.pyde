"""
Summary: This interactive sketch processes a portrait 
image to create a three-tiered visual effect based on brightness, 
influenced by mouse X position, showcasing areas of high, 
medium, and low brightness in white, gray, and black respectively.
"""
import random

# Canvas dimensions
canvas_width = 500
canvas_height = 750

# Brightness offset for creating tiers
offset = 100

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the initial background color to black.
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
    # Map the mouseX position to a brightness cutoff.
    cut = map(mouseX, 0, canvas_width, 0, 255)
    
    # Define high and low brightness cutoffs.
    cut_high = cut
    cut_low = cut - offset
    
    # Iterate over all pixels in the canvas.
    for i in range(total_pixels):
        # Get the brightness value of the current pixel.
        value = brightness(pixels[i])
        # Assign colors based on the pixel's brightness relative to the cutoffs.
        if value > cut_high:
            pixels[i] = color(255)  # High brightness pixels turn white.
        elif cut_low < value <= cut_high:
            pixels[i] = color(150)  # Medium brightness pixels turn gray.
        else:
            pixels[i] = color(0)  # Low brightness pixels turn black.
    
    # Update the canvas with the modified pixels.
    updatePixels()
