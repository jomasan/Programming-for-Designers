"""
Summary: This interactive sketch resamples a portrait 
image based on the mouse X position, dynamically adjusting 
the resolution of a pixelated representation to create 
varying levels of abstraction.
"""
import random

# Canvas dimensions
canvas_width = 500
canvas_height = 750

# Range of pixels to consider
pixel_range = 20

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
    global pixel_range
    # Redisplay the image each frame for dynamic interaction.
    image(img, 0, 0, 500, 750)
    
    # Dynamically adjust the pixel scale based on mouse X position.
    pixel_scale = map(mouseX, 0, canvas_width, 0.01, 0.3)
    # Calculate the resolution based on pixel_scale.
    res_x = canvas_width * pixel_scale
    res_y = canvas_height * pixel_scale
    # Determine the size of each "pixel" in the abstracted image.
    pixel_size = canvas_width / res_x
    
    # Debug output to console.
    println("res_x: " + str(res_x))
    println("pixel_scale: " + str(pixel_scale))
    
    # Iterate over the calculated resolution to draw the abstracted image.
    for i in range(int(res_x) + 1):
        for j in range(int(res_y) + 1):
            # Calculate the position for each "pixel".
            x = i * pixel_size
            y = j * pixel_size
            # Get the color from the original image at this position.
            col = img.get(int(x), int(y))
            fill(col)
            # Optionally draw a border around each "pixel".
            stroke(255, 10)
            # Draw a rectangle to represent the pixel.
            rect(x, y, pixel_size, pixel_size)
