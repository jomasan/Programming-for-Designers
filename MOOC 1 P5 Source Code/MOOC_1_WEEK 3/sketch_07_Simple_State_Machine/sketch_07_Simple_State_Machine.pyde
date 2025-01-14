"""
Summary: This code cycles through colors (red, green, blue) 
for an ellipse drawn on the canvas, changing the color with each mouse click 
to demonstrate a basic state machine.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

# Define a tuple with color states
states = ("RED", "GREEN", "BLUE")
# Set the initial color state
current_state = states[0]
# Define the position of the ellipse
x = 600
y = 300

def setup():
    # Create a canvas with the specified width and height
    size(canvas_width, canvas_height)

    # Set the initial fill color to red and disable stroke
    noStroke()
    fill(255, 0, 0)
    
def draw():
    # Make x and y global to access them inside this function
    global x, y
    
    # Set the background color to black and draw an ellipse
    background(0)
    ellipse(x, y, 200, 200)

def mouseClicked():
    # Call change_state function when the mouse is clicked
    change_state()
    
def change_state():
    # Access the global variables states and current_state
    global states, current_state
    
    # Change the current_state and fill color based on the current_state
    if (current_state == states[0]):
        current_state = states[1]
        fill(0, 255, 0)
    elif (current_state == states[1]):
        current_state = states[2]
        fill(0, 0, 255)
    elif (current_state == states[2]):
        current_state = states[0]
        fill(255, 0, 0)
    
    # Print the current state to the console
    print("CURRENT STATE: " + current_state)
