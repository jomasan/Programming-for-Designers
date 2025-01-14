#EXAMPLE OF BALL MOVING USING VECTOR MATH
#VECTOR ADDITION

#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#Define a vector that will represent a position
vec_position = PVector (500,200,0)

#Define a vector that will represent a velocity
vec_velocity = PVector (0,0,0)

#Define a vector that will represent a acceleration
vec_acceleration = PVector (0,0,0)

#Define a variable for the size of the rectangle
rec_size = 50

#Lets create a list of possible movements (up, right, down, left)
possible_velocities = []
possible_velocities.append (PVector (5,0,0))
possible_velocities.append (PVector (0,5,0))
possible_velocities.append (PVector (-5,0,0))
possible_velocities.append (PVector (0,-5,0))

#Define a variable that will determine the current direction being used
int_current_vel_index = 0

#Define the current velocity as one of the possible orientations
vec_velocity = possible_velocities[int_current_vel_index]

#Define the R,G,B values of a color
r = 0
g = 100
b = 255

#Define the rate of change of the colors
rchange = 1
gchange = 3
bchange = 5

#Functions
#1 - Change direction
def changeDirection():
    #Access global variables
    global vec_velocity, int_current_vel_index

    #change velocity to the next one in the list
    int_current_vel_index += 1

    #let's make sure we don't try to access an element outside the array.
    if int_current_vel_index > 3:
        int_current_vel_index = 0

    #Now let's replace the current velocoty for the next velocity in the list
    vec_velocity = possible_velocities[int_current_vel_index]


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

    #every 25 frame change direction
    if(frameCount % 25 ==0): changeDirection()

    #Vector addition
    vec_position.add(vec_velocity)

    #Draw the rectangle in the updated position
    rect(vec_position.x, vec_position.y, rec_size, rec_size)
    


  
