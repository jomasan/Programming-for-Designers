import random

# Definition of a class
class Discrete_Walker(object):
    # DocString
    '''Rectangle that moves discretely, changing color as a gradient'''

    # Class attributes for initial setup
    vec_position = PVector(500,200,0)  # Initial position
    vec_velocity = PVector(0,0,0)  # Initial velocity, starts stationary
    vec_acceleration = PVector(0,0,0)  # Initial acceleration, none
    rec_size = 50  # Size of the rectangle

    # Array of possible movements: up, right, down, left
    possible_velocities = [PVector(5,0,0), PVector(0,5,0), PVector(-5,0,0), PVector(0,-5,0)]

    int_next_flip = 25  # Frames until next direction change

    int_current_vel_index = 0  # Current velocity index from possible_velocities
    vec_velocity = possible_velocities[int_current_vel_index]  # Set initial velocity

    # Initial RGB color and changes per frame
    r = 0
    g = 100
    b = 255
    rchange = 1
    gchange = 3
    bchange = 5

    # Canvas bounds
    x_max = 0
    y_max = 0

    # Constructor - initializes instance variables
    def __init__(self, vec_position, rec_size, vec_velocity, r, g, b, x_max, y_max):
        self.vec_position = vec_position  # Position vector
        self.rec_size = rec_size  # Rectangle size
        self.vec_velocity = vec_velocity  # Velocity vector
        self.x_max = x_max  # Max x bound
        self.y_max = y_max  # Max y bound
        self.r = r  # Red color component
        self.g = g  # Green color component
        self.b = b  # Blue color component

    # Dashboard function to control walker actions
    def run(self):
        self.move()
        self.draw()
        self.bouce_color()
        self.flip_direction()
        self.stay_within_canvas()
    
    # Draw rectangle on screen
    def draw(self):
        noStroke()
        fill(self.r, self.g, self.b)
        rect(self.vec_position.x, self.vec_position.y, self.rec_size, self.rec_size)
    
    # Update position based on velocity
    def move(self):
        self.vec_position.add(self.vec_velocity)

    # Change direction at intervals
    def flip_direction(self):
        if frameCount % self.int_next_flip == 0:  # Check if it's time to change direction
            self.change_direction()

    # Change color dynamically
    def bouce_color(self):
        # Adjust color values
        self.r += self.rchange
        self.g += self.gchange
        self.b += self.bchange

        # Reverse color change direction if bounds are exceeded
        if self.r < 0 or self.r > 255: self.rchange *= -1
        if self.g < 0 or self.g > 255: self.gchange *= -1
        if self.b < 0 or self.b > 255: self.bchange *= -1

    # Randomly change direction of movement
    def change_direction(self):
        self.int_current_vel_index = (self.int_current_vel_index + 1) % len(self.possible_velocities)  # Cycle through possible directions
        self.int_next_flip = random.randrange(1, 40)  # Randomize time until next direction change
        self.vec_velocity = self.possible_velocities[self.int_current_vel_index]  # Update velocity

    # Ensure the rectangle stays within the canvas bounds
    def stay_within_canvas(self):
        # Reverse velocity if edges are reached
        if self.vec_position.x > self.x_max or self.vec_position.x < 0:
            self.vec_velocity.x *= -1
        if self.vec_position.y > self.y_max or self.vec_position.y < 0:
            self.vec_velocity.y *= -1
        # Adjust position to stay within bounds
        self.vec_position.x = min(max(self.vec_position.x, 0), self.x_max)
        self.vec_position.y = min(max(self.vec_position.y, 0), self.y_max)
