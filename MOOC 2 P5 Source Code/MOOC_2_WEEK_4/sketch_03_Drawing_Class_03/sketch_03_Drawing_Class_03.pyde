#EXAMPLE OF A CLASS TO DRAW A GRADIENT RECTANGLE

#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

##-----------------------------------------------------------------------------------------
#Class syntax
#Declare a class
class Gradient_Rectangle(object):

    #Docstring
    '''Rectangle for creating a gradient'''

    #Class functions
    #Constructor - variables to initiate the class
    def __init__(self, vec_position, rec_size, vec_velocity, color): # constructor
        self.vec_position = vec_position 
        self.rec_size = rec_size  
        self.vec_velocity = vec_velocity
        self.color = color
    
    #other class functions
    #display the class in the screen based on it's internal data
    def draw(self):
        noStroke()
        fill(self.color)
        rect(self.vec_position.x, self.vec_position.y, self.rec_size, self.rec_size)

    #move Function
    def move(self):
        self.vec_position.add(self.vec_velocity)

##-----------------------------------------------------------------------------------------

#create 3 objects from the  same class but with different data - let's try to be more explicit to what each argument represents:
G_R_1 = Gradient_Rectangle(vec_position = PVector (50,50,0) ,
                           rec_size = 50, 
                           vec_velocity = PVector (1,0,0), 
                           color = color(255,0,0)
                           )

G_R_2 = Gradient_Rectangle(vec_position = PVector (50,110,0) ,
                           rec_size = 50, 
                           vec_velocity = PVector (0.5,0,0), 
                           color = color(0,255,0)
                           )

G_R_3 = Gradient_Rectangle(vec_position = PVector (50,170,0) ,
                           rec_size = 50, 
                           vec_velocity = PVector (0.2,0,0), 
                           color = color(0,0,255)
                           )


def setup():

    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)

   
def draw():
    #Let's call the functions draw and move for the 3 instances of the class
    G_R_1.draw() 
    G_R_1.move()

    G_R_2.draw()
    G_R_2.move()

    G_R_3.draw()
    G_R_3.move()
    


  








    
    
