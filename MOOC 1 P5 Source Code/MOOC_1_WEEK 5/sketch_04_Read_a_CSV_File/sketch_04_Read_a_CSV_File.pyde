"""
Summary: This script reads color and position data 
from a CSV file named 'Data.csv', then draws ellipses 
on the canvas according to the read values, 
effectively visualizing the dataset.
"""
import random
import csv

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the background color to black.
    background(0)
    
    # Open 'Data.csv' for reading and use the csv.reader to iterate through rows.
    with open("Data.csv") as csvfile:
        data = csv.reader(csvfile)
        
        # Skip the header row.
        next(data)
        
        # Iterate through each row in the CSV file.
        for row in data:
            # Parse the x, y positions and RGB color values from the row.
            x = float(row[0])
            y = float(row[1])
            r = float(row[2])
            g = float(row[3])
            b = float(row[4])
                   
            # Set the fill color using the RGB values from the CSV.
            fill(r, g, b)
            # Draw an ellipse at the specified position with a fixed size.
            ellipse(x, y, 20, 20)
