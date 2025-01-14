"""
Summary: This code animates a rectangle moving in a square pattern on the canvas, 
changing direction with each mouse click to demonstrate directional state management.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

# Define a tuple with movement states
states = ("UP", "RIGHT", "DOWN", "LEFT")  
current_state = states[1]  # Start moving to the RIGHT
x = 600  # Initial x position
y = 300  # Initial y position

move_x = 1  # Initial x movement direction
move_y = 0  # Initial y movement direction

speed = 1  # Initial speed

def setup():
    # Initialize the canvas with the specified width and height
    size(canvas_width, canvas_height)
    background(0)  # Set background to black
    noStroke()  # Disable stroke for shapes
    fill(255, 0, 0)  # Set initial fill color to red
    
def draw():
    global x, y, move_x, move_y, speed
    
    # Create a fading effect by drawing a semi-transparent rectangle over the entire canvas
    fill(0, 20)
    rect(0, 0, canvas_width, canvas_height)
    
    # Set the fill color to white for the moving rectangle
    noStroke()
    fill(255)
    
    # Update the position of the rectangle based on the current movement direction and speed
    x += move_x * speed
    y += move_y * speed
    
    # Gradually increase the speed
    speed += 0.01
    
    # Draw the rectangle at the new position
    rect(x, y, 30, 30)

def mouseClicked():
    # Change the direction of movement when the mouse is clicked
    change_state()
    
def change_state():
    global states, current_state, move_x, move_y, speed
    
    # Change the current state based on the current direction of movement
    if (current_state == states[0]):  # UP
        current_state = states[1]
        move_x = speed
        move_y = 0
    elif (current_state == states[1]):  # RIGHT
        current_state = states[2]
        move_x = 0
        move_y = speed
    elif (current_state == states[2]):  # DOWN
        current_state = states[3]  
        move_x = -speed
        move_y = 0
    elif (current_state == states[3]):  # LEFT 
        current_state = states[0]
        move_x = 0
        move_y = -speed

    # Print the current state to the console
    print("CURRENT STATE: " + current_state)
