"""
Summary: This interactive sketch modifies the pixels 
of a displayed portrait image based on mouse X position, 
turning pixels within a narrow brightness range around 
the mapped cutoff to white, and all others to black, 
creating a dynamic visual effect.
"""
import random

# Canvas dimensions
canvas_width = 500
canvas_height = 750

# Brightness offset for creating a range
offset = 5

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the background color to black.
    background(0)
    
    # Load and display a portrait image onto the canvas.
    global img
    img = loadImage("portrait.jpg")
    image(img, 0, 0, 500, 750)
    
    # Prepare for pixel manipulation.
    loadPixels()
    global total_pixels
    total_pixels = canvas_width * canvas_height

def draw():
    # Redisplay the image for dynamic interaction.
    image(img, 0, 0, 500, 750)
    loadPixels()
    # Map the mouseX position to a brightness cutoff.
    cut = map(mouseX, 0, canvas_width, 0, 255)
    
    # Create upper and lower bounds for the brightness cutoff.
    cut_plus = cut + offset
    cut_minus = cut - offset
    
    # Iterate through all pixels in the canvas.
    for i in range(total_pixels):
        # Get the brightness value of the current pixel.
        value = brightness(pixels[i])
        # Change the pixel color based on whether its brightness falls within the specified range.
        if cut_minus < value < cut_plus:
            pixels[i] = color(255)  # Pixels within the range turn white.
        else:
            pixels[i] = color(0)  # Pixels outside the range turn black.
    
    # Update the canvas with the modified pixels.
    updatePixels()
