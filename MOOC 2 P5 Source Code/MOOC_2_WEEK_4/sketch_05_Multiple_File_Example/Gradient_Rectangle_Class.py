# Define a class named Gradient_Rectangle. 
# This class is meant to create and manage rectangles with gradient coloring.
class Gradient_Rectangle(object):
    '''Rectangle for creating a gradient'''

    # The __init__ method is the constructor for the class. It initializes a new instance of the class.
    def __init__(self, vec_position, rec_size, vec_velocity, color):
        # self.vec_position stores the position of the rectangle as a PVector.
        self.vec_position = vec_position
        # self.rec_size stores the size of the rectangle. This value is used for both the width and height, making the rectangle a square.
        self.rec_size = rec_size
        # self.vec_velocity stores the velocity of the rectangle as a PVector, determining how it moves.
        self.vec_velocity = vec_velocity
        # self.color stores the color of the rectangle.
        self.color = color
    
    # The draw method is responsible for displaying the rectangle on the screen.
    def draw(self):
        noStroke()  # Disables drawing the stroke (outline) around the rectangle.
        fill(self.color)  # Sets the fill color to the rectangle's color.
        # Draws the rectangle at the position specified by vec_position.x and vec_position.y, with the size specified by rec_size.
        rect(self.vec_position.x, self.vec_position.y, self.rec_size, self.rec_size)

    # The move method updates the rectangle's position by adding the velocity to the current position.
    def move(self):
        self.vec_position.add(self.vec_velocity)  # Add the velocity vector to the position vector, moving the rectangle.
