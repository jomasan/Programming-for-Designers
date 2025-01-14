"""
Summary: This code draws two rectangles on a canvas, 
the first at the top-left corner, and the second at the center, 
demonstrating the use of the translate function to change the origin for drawing.
"""
# Canvas dimensions
canvas_width = 1200
canvas_height = 600

def setup():
    # Initialize the canvas with the specified width and height.
    size(canvas_width, canvas_height)
    # Set the background color to black.
    background(0)
    # Set the fill color for rectangles to green.
    fill(0,255,0)
    # Set the stroke color for rectangles to white.
    stroke(255)
    
    # Draw the first rectangle at the top-left corner of the canvas.
    rect(0, 0, 30, 40)
    
    # Change the current position for drawing to the center of the canvas.
    translate(600, 300)
    
    # Draw the second rectangle, now positioned at the center due to the translate function.
    rect(0, 0, 30, 40)
