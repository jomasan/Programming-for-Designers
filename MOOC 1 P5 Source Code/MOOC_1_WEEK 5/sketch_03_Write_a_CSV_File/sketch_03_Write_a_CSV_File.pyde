"""
Summary: This script generates 500 random 
colored ellipses on a canvas and records 
their positions and color values in a CSV file 
named 'Data.csv', with headers for x, y, Red, Green, and Blue values.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the background color to black.
    background(0)
    
    # Create a writer to output data to a CSV file.
    output = createWriter("Data.csv")
    
    # Write the header row to the CSV file.
    output.println("x, y, Red, Green, Blue")
        
    # Generate 500 ellipses with random positions and colors.
    for i in range(500):
        # Randomly determine the position for each ellipse.
        x = random.randrange(0, canvas_width)
        y = random.randrange(0, canvas_height)
        
        # Randomly determine the color for each ellipse.
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        
        # Set the fill color and draw the ellipse.
        fill(r, g, b)
        ellipse(x, y, 20, 20)
        
        # Write the ellipse's data to the CSV file.
        output.println(f"{x}, {y}, {r}, {g}, {b}")
    
    # Ensure all data is written and close the file.
    output.flush()
    output.close()
