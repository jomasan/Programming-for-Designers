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
vec_velocity = PVector (10,0,0)

#Define a variable for the size of the rectangle
rec_size = 50

#Define the R,G,B values of a color
r = 0
g = 100
b = 255

#Define the rate of change of the colors
rchange = 1
gchange = 3
bchange = 5

def setup():

    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)

   
def draw():

    #Access to global variables
    global vec_position, vec_velocity
    global r,g,b
    global rchange,gchange, bchange
    
    #OPTIONAL - FADE EFFECT:
    #fill(0,5)
    #rect(0,0,image_size_x,image_size_y)

    #Define the color of the geometry
    noStroke()
    fill(r,g,b)

    #Define the rate of change of the colors
    r += rchange
    g += gchange
    b += bchange

    #Make sure that the color values stay within the bounds of a color spectrum - 0 - 255
    if(r < 0) : rchange *= -1
    if(r > 255) : rchange *= -1
    if(g < 0) : gchange *= -1
    if(g > 255) : gchange *= -1
    if(b < 0) : bchange *= -1
    if(b > 255) : bchange *= -1

    #Let's define a vector with the mouse's position
    mousePos = PVector(mouseX, mouseY)

    #And we'll initialize a variable that will represent the difference bewtween the object and the mouse - we'll start with the mouse position vector
    vec_difference = mousePos

    #Use vector substraction to determine the vector between the 2 objects
    vec_difference.sub(vec_position)

    #Vector normalization scales the magnitude of the vector to 1
    vec_difference.normalize()

    #Vector multiplication scales the vector to our desired size, here it is 2
    vec_difference.mult(2)
      
    #Use vector addition to add the new difference vector as a motion vector
    vec_position.add(vec_difference)

    #draw the ellipse in the updated position
    ellipse(vec_position.x, vec_position.y, rec_size, rec_size)
    


  








    
    
