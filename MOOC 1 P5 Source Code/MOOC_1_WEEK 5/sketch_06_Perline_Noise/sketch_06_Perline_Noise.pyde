"""
Summary: This script visualizes Perlin noise across a 2D grid 
by dynamically adjusting the noise scale and detail based on 
the mouse position, creating a complex pattern of grayscale squares.
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
    
    # Iterate over a grid of 120x120.
    for i in range(120):
        for j in range(120):
            # Calculate the x and y positions for each square in the grid.
            x = i * 5
            y = j * 5
            
            # Uncomment the following line to dynamically adjust noise scale based on mouseX position.
            # noiseScale = map(mouseX, 0, canvas_width, 0, 1)
            noiseScale = 0.0074
            # Adjust level of detail (lod) based on mouseY position.
            lod = int(map(mouseY, 0, canvas_height, 1, 10))
            # Adjust falloff based on mouseX position for smoother or more abrupt transitions.
            falloff = map(mouseX, 0, canvas_width, 0, 1)
            # Set noise detail with the calculated level of detail and falloff.
            noiseDetail(lod, falloff)
            # Calculate noise value for each square and map it to a grayscale color.
            n = noise(x * noiseScale, y * noiseScale) * 100
            noStroke()
            fill(n)
            
            # Draw a rectangle at the calculated position with a fixed size.
            rect(x, y, 5, 5)
