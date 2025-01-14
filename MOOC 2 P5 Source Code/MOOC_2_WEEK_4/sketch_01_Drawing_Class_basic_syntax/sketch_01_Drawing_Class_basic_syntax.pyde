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
    def __init__(self, vec_position, rec_size): 
        self.vec_position = vec_position 
        self.rec_size = rec_size  
    
    #other class functions
    #display the class in the screen based on it's internal data
    def draw(self):
        noStroke()
        fill(255,0,0)
        rect(self.vec_position.x, self.vec_position.y, self.rec_size, self.rec_size)

##-----------------------------------------------------------------------------------------

#Create the instance of a class -> an Object or an Instance
G_R_01 = Gradient_Rectangle(
                            vec_position = PVector (50,50,0) , 
                            rec_size = 50
                            )

def setup():

    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)

   
def draw():

    #Call functions from the object we created
    G_R_01.draw()
    
    


  








    
    
