
#Definition of a class
class Gradient_Circle(object):
    '''Circle for creating a gradient'''

    #Constructor - arguments that are required to create an instance of this class
    def __init__(self, vec_position, rec_size, vec_velocity, color): 
        #association of class variables with incoming arguments from the constructor
        self.vec_position = vec_position 
        self.rec_size = rec_size  
        self.vec_velocity = vec_velocity
        self.color = color
    
    #Functions ------

    #Function for the class to draw itself in the canvas based on it's internal attributes
    def draw(self):
        noStroke()
        fill(self.color)
        ellipse(self.vec_position.x, self.vec_position.y, self.rec_size, self.rec_size)

    #Function to make the class move based on it's velocity vector
    def move(self):
        self.vec_position.add(self.vec_velocity)


    
    


  








    
    
