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

#Create an empty list 
myList = []

#variable that define the total number of elements
num_cols = 50

def setup():

    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)

    #Loop to generate a series of instances of the class and store them in the list
    for i in range(0,num_cols):

        #arguments for the constructor
        c_size = (image_size_y / num_cols) #size of the the rectangle
        c_pos_y = (c_size * i) # position in y
        rand_color = color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)) #random color
        rand_speed = random.uniform(0.01,1) #random speed

        #Create the instance of the class
        G_R_1 = Gradient_Rectangle(vec_position = PVector (0,c_pos_y,0) , 
                                   rec_size = c_size, 
                                   vec_velocity = PVector (rand_speed,0,0), 
                                   color = rand_color
                                   )
                                   
        #Add the instance of the class to the list                      
        myList.append(G_R_1)

   
def draw():

    #Execute the functions for all elements inside the list
    for x in myList:
        x.draw()
        x.move()

    


  








    
    
