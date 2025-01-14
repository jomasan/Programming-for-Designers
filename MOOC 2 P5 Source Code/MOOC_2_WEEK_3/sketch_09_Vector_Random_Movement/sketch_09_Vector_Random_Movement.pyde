#EXAMPLE OF BALL MOVING USING VECTOR MATH
#VECTOR ADDITION

#import the random module
import random

# Canvas dimensions
image_size_x = 2400
image_size_y = 1200

#Define a vector that will represent a position
vec_position = PVector (500,200,0)

#Define a vector that will represent a velocity
vec_velocity = PVector (0,0,0)

#Define a vector that will represent a acceleration
vec_acceleration = PVector (0,0,0)

#Define a variable for the size of the rectangle
rec_size = 50

#Lets create an array of possible movements (up, right, down, left)
possible_velocities = []
possible_velocities.append (PVector (5,0,0))
possible_velocities.append (PVector (0,5,0))
possible_velocities.append (PVector (-5,0,0))
possible_velocities.append (PVector (0,-5,0))

#Let's create a timer variable to define when the next change of orientation will happen
int_next_flip = 50

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
def change_direction():
    #Access global variables
    global vec_velocity, int_current_vel_index, int_next_flip

    #change velocity to the next one in the list
    int_current_vel_index += 1

    #let's make sure we don't try to access an element outside the array.
    if int_current_vel_index > 3:
        int_current_vel_index = 0
    
    #Define the time for the next change of orientation based on a random range
    int_next_flip = random.randrange(1,40)

    #Now let's replace the current velocoty for the next velocity in the list
    vec_velocity = possible_velocities[int_current_vel_index]

#2 - Stay within the canvas
def stay_within_canvas():
    #Lets flip the velocity vector in case the ball reaches the edge of the screen
    if vec_position.x > image_size_x:
        vec_velocity.x *= -1
        vec_position.x = image_size_x
    
    if vec_position.x < 0:
        vec_velocity.x *= -1
        vec_position.x = 0
    
    if vec_position.y <= 0:
        vec_velocity.y *= -1
        vec_position.y = 0
    
    if vec_position.y > image_size_y:
        vec_velocity.y *= -1
        vec_position.y = image_size_y


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

    #change direction once we reach the number of frame defined by the next flip variable
    if(frameCount % int_next_flip ==0): change_direction()

    #call the function to stay within the canvas
    stay_within_canvas()

    #Vector addition - update the position of the rectangle
    vec_position.add(vec_velocity)

    #draw the rectangle
    rect(vec_position.x, vec_position.y, rec_size, rec_size)
    


  
