#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#define the resolution of a grid
reso_x = 100
reso_y = 50

#Variable to store the current position of a 'walker'
int_current_index_x = 20
int_current_index_y = 20

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y)

    # Create a black background
    background(0,0,0)

    #Define the size of a Cell by dividing the size of the screen by the resolution of the grid
    cell_size_x = image_size_x / reso_x
    cell_size_y = image_size_y / reso_y

    #We'll do a nested loop - one loop for our iteration in X and another for Y
    for i in range(0, reso_x):
        for j in range(0, reso_y):

            #Define the position of a cell by the i and j iteration provided in the loop, multiplied by the size of the cell
            pos_x = (i * cell_size_x) 
            pos_y = (j * cell_size_y)

            #Define a random color for red, green and blue channels
            c_red = random.randrange(0,255)
            c_green = random.randrange(0,255)
            c_blue = random.randrange(0,255)
        
            #draw a rectangle 
            noStroke()
            fill(c_red, c_green, c_blue)
            rect(pos_x, pos_y, cell_size_x, cell_size_y)


def draw():

    #Recalculate the Cell size for the draw loop
    cell_size_x = image_size_x / reso_x
    cell_size_y = image_size_y / reso_y
    
    #Random Walk 
    #Get access to global variables
    global int_current_index_x
    global int_current_index_y

    #increase the x coordinate by +1 or -1 at random
    int_current_index_x += random.randint(-1,1)
    #increase the y coordinate by +1 or -1 at random
    int_current_index_y += random.randint(-1,1)

    #Stay within bounds - make sure that the index of the walker is within the bounds of the grid
    if int_current_index_x < 0 : int_current_index_x = 0
    if int_current_index_x >= reso_x : int_current_index_x = reso_x
    if int_current_index_y < 0 : int_current_index_y = 0
    if int_current_index_y >= reso_y : int_current_index_y = reso_y

    #Define the actual position of the walker by multiplying the index position by the cell size
    pos_x = (int_current_index_x * cell_size_x) 
    pos_y = (int_current_index_y * cell_size_y)

    #Let's hard code the color white, but we could use anothe color for the walker. White will make it more visible among all the other colors
    c_red = 255     
    c_green = 255   
    c_blue = 255    

    #draw a rectangle representing the walker in the position calculated
    noStroke()
    fill(c_red, c_green, c_blue)
    rect(pos_x, pos_y, cell_size_x, cell_size_y)

    #Optional: Print the index coordinate of the walker
    #println(int_current_index_x + "," + int_current_index_y)
 
