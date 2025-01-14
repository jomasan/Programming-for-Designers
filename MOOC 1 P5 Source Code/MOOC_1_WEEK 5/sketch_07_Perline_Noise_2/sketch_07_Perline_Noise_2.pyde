"""
Summary: This script generates a 2D Perlin noise pattern 
across a grid, with each square's fill based on a threshold 
function that creates a stark black and white contrast, 
controlled by mouse position.
"""
import random

# Canvas dimensions
canvas_width = 600
canvas_height = 600

# Initial noise scale
noiseScale = 0.02

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the initial background color to black.
    background(0)

def draw():
    global noiseScale
    
    # Iterate over a grid to draw squares.
    for i in range(120):
        for j in range(120):
            # Calculate the x and y positions for each square.
            x = i * 5
            y = j * 5
            
            # Set the noise scale. Uncomment the following line to adjust dynamically with mouseX.
            # noiseScale = map(mouseX, 0, canvas_width, 0, 1)
            noiseScale = 0.0074
            # Adjust the level of detail and falloff based on mouse position.
            lod = int(map(mouseY, 0, canvas_height, 1, 10))
            falloff = map(mouseX, 0, canvas_width, 0, 1)
            noiseDetail(lod, falloff)
            # Calculate noise value at each point.
            n = noise(x * noiseScale, y * noiseScale)
            
            # Map the noise value to a grayscale and then apply a threshold.
            mapped_noise = map(n, 0, 1, 0, 255)
            threshold_noise = threshold(n, 0.5)
            
            noStroke()
            fill(threshold_noise)
            
            # Draw the square with the calculated fill.
            rect(x, y, 5, 5)

# Define a threshold function to convert noise to black or white.
def threshold(value, cutoff):
     return 255 if value >= cutoff else 0
