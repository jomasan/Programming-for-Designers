import random

#Definition of a class
class Discrete_Walker(object):
    #DocString
    '''Rectangle that moves Discretely, changing color as a gradient'''

    # Static class attributes initialization
    vec_position = PVector(500,200,0)  # Starting position of the rectangle
    vec_velocity = PVector(0,0,0)  # Initial velocity (stationary)
    vec_acceleration = PVector(0,0,0)  # Initial acceleration (none)
    rec_size = 50  # Size of the rectangle

    #Lets create an array of possible movements (up, right, down, left)
    possible_velocities = []
    possible_velocities.append (PVector (5,0,0))
    possible_velocities.append (PVector (0,5,0))
    possible_velocities.append (PVector (-5,0,0))
    possible_velocities.append (PVector (0,-5,0))

    int_next_flip = 25

    int_current_vel_index = 0
    vec_velocity = possible_velocities[int_current_vel_index]

    # Color attributes and their change rates
    r = 0  # Red component of color
    g = 100  # Green component of color
    b = 255  # Blue component of color
    rchange = 1  # Change rate for red component
    gchange = 3  # Change rate for green component
    bchange = 5  # Change rate for blue component

    # Canvas dimensions to limit movement
    x_max = 0
    y_max = 0

    #Constructor - arguments that are required to create an instance of this class
    def __init__(self, vec_position, rec_size, vec_velocity, r,g,b, x_max, y_max): # constructor
        self.vec_position = vec_position  # Position vector
        self.rec_size = rec_size  # Rectangle size
        self.vec_velocity = vec_velocity  # Velocity vector
        self.x_max = x_max  # Maximum X boundary
        self.y_max = y_max  # Maximum Y boundary
        self.r = r  # Red color component
        self.g = g  # Green color component
        self.b = b  # Blue color component

    #Functions ------

    #Function run will be a 'dashboard' that will call all other classes that build the behavior of this class
    def run(self):
        self.move()
        self.draw()
        self.bounce_color()
        self.flip_direction()
        self.stay_within_canvas()
    
    #Draw the graphic in the screen
    def draw(self):
        noStroke()
        fill(self.r,self.g,self.b)
        rect(self.vec_position.x, self.vec_position.y, self.rec_size, self.rec_size)
    
    #Move function based on velocity data
    def move(self):
        self.vec_position.add(self.vec_velocity)

    
    def flip_direction(self):
         #every 25 frame change direction
        if(frameCount % self.int_next_flip == 0): self.change_direction()


    def bounce_color(self):
        self.r += self.rchange
        self.g += self.gchange
        self.b += self.bchange

        # Inverts the change direction if limits are reached
        if self.r < 0 or self.r > 255: self.rchange *= -1
        if self.g < 0 or self.g > 255: self.gchange *= -1
        if self.b < 0 or self.b > 255: self.bchange *= -1
    
    def change_direction(self):
        #change velocity to the next one in the list
        self.int_current_vel_index += 1

        #let's make sure we don't try to access an element outside the array.
        if self.int_current_vel_index > 3:
            self.int_current_vel_index = 0
        
        self.int_next_flip = random.randrange(1,40)

        self.vec_velocity = self.possible_velocities[self.int_current_vel_index]

    def stay_within_canvas(self):
        #Lets flip the velocity vector in case the ball reaches the edge of the screen
        if self.vec_position.x > self.x_max:
            self.vec_velocity.x *= -1
            self.vec_position.x = self.x_max
        
        if self.vec_position.x < 0:
            self.vec_velocity.x *= -1
            self.vec_position.x = 0
        
        if self.vec_position.y <= 0:
            self.vec_velocity.y *= -1
            self.vec_position.y = 0
        
        if self.vec_position.y > self.y_max:
            self.vec_velocity.y *= -1
            self.vec_position.y = self.y_max


    
    


  








    
    
