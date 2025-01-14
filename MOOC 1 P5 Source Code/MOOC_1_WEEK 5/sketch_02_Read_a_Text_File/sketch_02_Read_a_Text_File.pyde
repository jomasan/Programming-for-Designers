"""
Summary: This script initializes a canvas and reads 
data from a text file named 'Data.txt', 
printing each line to the console until the end of the file is reached.
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

    # Attempt to create a reader for the 'Data.txt' file.
    try:
        reader = createReader("Data.txt")
        
        # Read the first line from the file.
        line = reader.readLine()
        
        # Continue reading lines until the end of the file is reached.
        while line != None:
            # Print the current line to the console.
            print(line)
            # Read the next line.
            line = reader.readLine()
    except Exception as e:
        # If an error occurs (e.g., file not found), print the error message.
        print("Error reading file:", e)
