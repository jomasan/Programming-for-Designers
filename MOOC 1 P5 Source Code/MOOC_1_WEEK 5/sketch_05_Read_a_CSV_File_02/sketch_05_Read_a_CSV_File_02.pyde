"""
Summary: This script reads color and position data from 'Data.csv', 
skipping the header line, then visualizes this data by drawing 
colored ellipses on a canvas based on the CSV values.
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
    
    # Attempt to create a reader for the 'Data.csv' file.
    try:
        reader = createReader("Data.csv")
        
        # Read and discard the header line.
        reader.readLine()
        
        # Read the next line to start processing data.
        line = reader.readLine()
        
        # Continue reading lines until the end of the file is reached.
        while line != None:
            # Split the line by commas to extract individual data elements.
            data = line.split(",")
            
            # Parse position and color values from the CSV data.
            x = float(data[0])
            y = float(data[1])
            r = float(data[2])
            g = float(data[3])
            b = float(data[4])
                   
            # Set the fill color using the parsed RGB values.
            fill(r, g, b)
            # Draw an ellipse at the specified position with a fixed size.
            ellipse(x, y, 20, 20)
            
            # Read the next line in the file.
            line = reader.readLine()
    except Exception as e:
        # If an error occurs (e.g., file not found), print the error message.
        print("Error reading file:", e)
