"""
Summary: This code implements a basic game where a rectangle moves around the screen, 
changing direction on mouse clicks, and the game ends (displaying "GAME OVER") 
if the rectangle moves beyond the canvas boundaries.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

# Define game states
game_states = ("PLAYING", "GAME OVER")
current_game_state = game_states[0]

# Define movement states
states = ("UP", "RIGHT", "DOWN", "LEFT") 
current_state = states[1]
x = 600
y = 300

move_x = 1
move_y = 0

speed = 1

def setup():
    # Initialize the canvas with the specified width and height
    size(canvas_width, canvas_height)
    background(0)
    noStroke()
    fill(255,0,0)
    
def draw():
    global x, y, move_x, move_y, speed
    
    # Create a fading effect by drawing a semi-transparent rectangle over the entire canvas
    fill(0,20)
    rect(0, 0, canvas_width, canvas_height)
    
    fill(255)
    
    if (current_game_state == game_states[0]):  # PLAYING
        # Move the rectangle according to the current movement state
        x += move_x
        y += move_y    
        speed += 0.01    
        rect(x, y, 30, 30)
        # Check for collisions with the canvas boundaries
        check_collision()
    elif (current_game_state == game_states[1]):  # GAME OVER
        # Display the game over screen
        fill(255,0,0)
        rect(0, 0, canvas_width, canvas_height)
        fill(255)
        textSize(40)
        text("GAME OVER", 520, 300)

def check_collision():
    global x, y, canvas_width, canvas_height, current_game_state
    # Check if the rectangle has moved beyond any canvas boundary
    if (x > canvas_width or x < 0 or y > canvas_height or y < 0):
        current_game_state = game_states[1]

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

    print("CURRENT STATE: " + current_state)
