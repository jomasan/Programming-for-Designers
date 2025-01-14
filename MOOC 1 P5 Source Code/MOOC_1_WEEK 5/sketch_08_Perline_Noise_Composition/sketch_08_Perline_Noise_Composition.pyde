"""
Summary: This script generates a dynamic Perlin noise-based 
pattern with adjustable scale and detail, featuring a moving 
effect influenced by mouseX and a threshold function for visual contrast.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

# Initial noise scale
noiseScale = 0.02

# Offset for moving the noise pattern
x_offset = 0

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the background color to black.
    background(0)

def draw():
    global noiseScale, x_offset
    
    # Dynamically adjust noise scale based on mouse X position.
    noiseScale = map(mouseX, 0, canvas_width, 0, 0.01)
    # Set a fixed level of detail and falloff for noise calculation.
    lod = 3
    falloff = 0.67
    
    # Set a fixed noise seed for consistent patterns.
    noiseSeed(1)
    
    # Iterate over the canvas in steps to draw small squares.
    for i in range(600):
        for j in range(120):
            # Calculate the position for each square.
            x = i * 2
            y = j * 5
                
            # Apply noise detail settings.
            noiseDetail(lod, falloff)
            # Calculate noise value at each point, adding an offset for motion.
            n = noise((x * noiseScale) + x_offset, y * noiseScale)
            
            # Apply a threshold function to determine fill color.
            threshold_range_noise = threshold_range(n, 0.5, 0.55)
            
            noStroke()
            fill(threshold_range_noise)
            
            # Draw the square with the calculated fill color.
            rect(x, y, 5, 5)
    
    # Increment the offset to create a moving effect.
    x_offset += 0.05

# Define a threshold function for simple black or white output.
def threshold(value, cutoff):
     return 255 if value >= cutoff else 0

# Define a threshold function with a range for more nuanced control over the output.
def threshold_range(value, cutoff1, cutoff2):
     return 255 if cutoff1 <= value <= cutoff2 else 0
