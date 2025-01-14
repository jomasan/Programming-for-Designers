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
    
    #Define the color of the geometry
    noStroke()
    fill(r,g,b)

    #Dynamically change the color of the rectangle based on the rate of change variables
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

    #shift direction once the rectangle gets closer to the edge
    if(vec_position.x > 1050):
        vec_velocity.x *= -1
        
    if(vec_position.x < 100):
        vec_velocity.x *= -1

    #The Normalize operation will make the vector to have a magnitude of 1
    vec_velocity.normalize()

    #We'll calculate the difference between the position of the rectangle and the x coordinate of the mouse
    x_dif_to_mouse = abs(vec_position.x - mouseX)

    #Using multiplication, we can scale the vector to our desired magniture - this is possible only if we use scale after normalizing the vector
    vec_velocity.mult( x_dif_to_mouse/10 )

    #Vector addition
    vec_position.add(vec_velocity)

    #Draw the rectangle
    rect(vec_position.x, vec_position.y-25, rec_size, rec_size * 2)
    


  








    
    
