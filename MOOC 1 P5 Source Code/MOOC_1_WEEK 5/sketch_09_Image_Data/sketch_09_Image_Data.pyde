"""
Summary: This script loads a portrait image onto a canvas, 
analyzes the brightness of each pixel, and alters the 
canvas pixels to display a red color for darker areas 
and white for lighter areas.
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
    
    # Load an image named 'portrait.jpg' and display it on the canvas.
    global img
    img = loadImage("portrait.jpg")
    image(img, 0, 0, 500, 750)
    
    # Load the current canvas pixels into the pixels array.
    loadPixels()
    total_pixels = canvas_width * canvas_height
    
    # Print the brightness of a specific pixel for debugging.
    println(brightness(img.get(200, 200)))
    
    # Iterate over all pixels in the canvas.
    for i in range(total_pixels):
        # Get the brightness value of the current pixel.
        value = brightness(pixels[i])
        # If the brightness is below 150, change the pixel to red.
        if value < 150:
            pixels[i] = color(255, 0, 0)
        # Otherwise, change the pixel to white.
        else:
            pixels[i] = color(255)
    
    # Update the canvas with the modified pixels array.
    updatePixels()
