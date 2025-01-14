#EXAMPLE OF BALL MOVING USING VECTOR MATH
#VECTOR ADDITION

#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#Define a vector that will represent a position
vec_position = PVector (100,300,0)

#Define a vector that will represent a velocity
vec_velocity = PVector (2,0,0)

#Define a variable for the size of the rectangle
rec_size = 50

#Define the R,G,B values of a color
r = 0
g = 100
b = 255

def setup():

    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y)

    # Create a black background
    background(0,0,0)

   
def draw():
    #Access to global variables
    global vec_position, vec_velocity
    global r,g,b
    
    #Define the color of the geometry
    noStroke()
    fill(r,g,b)

    #Draw the rectangle moving across the screen while within the specified coordinates
    if(vec_position.x < 1050):

        #Use Vector addition to generate motion
        vec_position.add(vec_velocity)

        #Draw the rectangle
        rect(vec_position.x, vec_position.y, rec_size, rec_size)
    


  








    
    
