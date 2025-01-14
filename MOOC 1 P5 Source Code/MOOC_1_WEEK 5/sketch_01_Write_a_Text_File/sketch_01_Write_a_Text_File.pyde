"""
Summary: This script creates a canvas and writes a series of numbers, 
including the results of a mock equation and 200 random numbers 
between 0 and 99, to a text file named 'Data.txt'.
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
    
    # Create a writer to output data to a text file.
    output = createWriter("Data.txt")
    
    # Write some predetermined numbers and a statement to the file.
    output.println(6)
    output.println(7)
    output.println(2)
    output.print(5)
    output.print(": is the result of the equation")
    
    # Generate and write 200 random numbers to the file.
    for i in range(200):
        output.println(random.randrange(0, 100))
    
    # Ensure all data is written to the file before closing.
    output.flush()
    # Close the writer to finalize the file.
    output.close()
