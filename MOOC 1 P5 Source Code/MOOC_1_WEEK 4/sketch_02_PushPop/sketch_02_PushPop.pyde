"""
Summary: This code demonstrates the use of pushMatrix() and popMatrix() 
to temporarily change the drawing origin for a rectangle to the center 
of the canvas, then draws another rectangle at the original top-left corner.
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
    
    # Save the current transformation matrix (drawing origin).
    pushMatrix()
    # Change the current position for drawing to the center of the canvas.
    translate(600, 300)
    # Draw a rectangle at the new origin (center of the canvas).
    rect(0, 0, 30, 40)
    # Restore the previous transformation matrix, returning to the original drawing origin.
    popMatrix()
    
    # Draw another rectangle at the top-left corner of the canvas.
    rect(0, 0, 30, 40)
