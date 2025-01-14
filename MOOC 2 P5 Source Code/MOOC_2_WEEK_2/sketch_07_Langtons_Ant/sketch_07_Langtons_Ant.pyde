#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#define the resolution of a grid
reso_x = 100
reso_y = 50

#Calculate the total number of cells
total_cells = reso_x * reso_y

#CELLS DATA - this list will store the data of each cell in the grid
cells = []

#Variable to store the current position of a 'walker'
int_current_index_x = 50
int_current_index_y = 25

#Create local variables for x and y to create a flat grid in a single loop
count_x = 0
count_y = 0

count = 50

#Declare the variables that will define the size of the cell
cell_size_x = 0
cell_size_y = 0

#Define a variable that will determine the direction of walk - 0, 1, 2, 3 - for all for cardinal directions
int_direction = 0

#Walker Functions
#Move Forward - add or substract to the index position depending on the orientation of the walker
def move_forward(dir):
    global int_current_index_x
    global int_current_index_y
    if(dir == 0):
        int_current_index_x += 1 #MOVE RIGHT
    elif(dir == 1):
        int_current_index_y += 1 #MOVE DOWN
    elif(dir == 2):
        int_current_index_x -= 1 #MOVE LEFT
    elif(dir == 3):
        int_current_index_y -= 1 #MOVE UP

#Rotate clockwise - change the direction variable dependening or your current direction
def rotate_clockwise_90():
    global int_direction
    if int_direction == 0 :
        int_direction = 1
    elif int_direction == 1 :
        int_direction = 2
    elif int_direction == 2 :
        int_direction = 3
    elif int_direction == 3 :
        int_direction = 0

#Rotate counter clockwise - change the direction variable dependening or your current direction
def rotate_counter_clockwise_90():
    global int_direction
    if int_direction == 0 :
        int_direction = 3
    elif(int_direction == 1):
        int_direction = 0
    elif(int_direction == 2):
        int_direction = 1
    elif(int_direction == 3):
        int_direction = 2

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)

    #Calculate the total number of cells
    total_cells = reso_x * reso_y

    #Populate the data of the list with a random integer, either 0 or 1
    for i in range(0,total_cells):
        cells.append ( 1 ) #Let's start will all cells with '1'

    #Define the size of a Cell by dividing the size of the screen by the resolution of the grid
    cell_size_x = image_size_x / reso_x
    cell_size_y = image_size_y / reso_y

    #Update local variables for x and y to create a flat grid in a single loop
    count_x = 0
    count_y = 0

    #Loop through the total number of cells
    for i in range(0, total_cells):

        #define the positions in x and y based on our local varible
        pos_x = (count_x * cell_size_x) 
        pos_y = (count_y * cell_size_y)

        noStroke()

        #We'll paint the cells black or white depending on the data that they have. 0 = black, 1 = white.
        if(cells [i] == 0): fill(0, 0, 0)
        if(cells [i] == 1): fill(255, 255, 255)
        
        #Let's do a rectangle of the defined color in the position of the grid
        rect(pos_x, pos_y, cell_size_x, cell_size_y)

        #Grid as a typewriter count
        count_x += 1
        if(count_x >= reso_x):
            count_y += 1
            count_x = 0


def draw():

    #Random Walk 
    #Get access to global variables
    global int_current_index_x
    global int_current_index_y

    #Stay within bounds - make sure that the index of the walker is within the bounds of the grid
    if int_current_index_x < 0 : int_current_index_x = 0
    if int_current_index_x >= reso_x : int_current_index_x = reso_x -1
    if int_current_index_y < 0 : int_current_index_y = 0
    if int_current_index_y >= reso_y : int_current_index_y = reso_y -1

    #Convert X and Y coordinates into the index of a flat list
    index = int_current_index_x + (int_current_index_y * reso_x)

    #Let's make sure that count x and y are back at 0
    count_x = 0
    count_y = 0

    #Redraw the cells
    for i in range(0, total_cells):

        #Recalculate the Cell size for the draw loop
        cell_size_x = image_size_x / reso_x
        cell_size_y = image_size_y / reso_y

        #Define the actual position of the walker by multiplying the index position by the cell size
        pos_x = (count_x * cell_size_x) 
        pos_y = (count_y * cell_size_y)

        noStroke()

        #We'll paint the cells black or white depending on the data that they have. 0 = black, 1 = white.
        if(cells [i] == 0): fill(0, 0, 0)
        elif(cells [i] == 1): fill(255, 255, 255)
        
        #Let's do a rectangle of the defined color in the position of the grid
        rect(pos_x, pos_y, cell_size_x, cell_size_y)

        #Grid as a typewriter count
        count_x += 1
        if(count_x >= reso_x):
            count_y += 1
            count_x = 0


    #Draw the walker agent (optional)
    fill(255,0,0)
    w_pos_x = (int_current_index_x * cell_size_x) + (cell_size_x/2)
    w_pos_y = (int_current_index_y * cell_size_y) + (cell_size_y/2)
    ellipse(w_pos_x,w_pos_y, 20, 20 )

    #Draw a line representing the orientation of the walker 
    arrow_size = 20
    stroke(255,0,0)
    strokeWeight(2)

    #Draw the line depending on the orientation
    if int_direction == 0: line(w_pos_x,w_pos_y,w_pos_x +arrow_size,w_pos_y)
    if int_direction == 1: line(w_pos_x,w_pos_y,w_pos_x ,w_pos_y + arrow_size)
    if int_direction == 2: line(w_pos_x,w_pos_y,w_pos_x -arrow_size,w_pos_y)
    if int_direction == 3: line(w_pos_x,w_pos_y,w_pos_x ,w_pos_y - arrow_size)
        
    #Behavior of the walker based on the cells data:

    #If Cell is white:
    if(cells [index] == 1): 
        rotate_clockwise_90()           #rotate clockwise
        cells [index] = 0               #flip the value of the cell
        move_forward(int_direction)     #move forward
    #If Cell is black
    elif (cells [index] == 0):
        rotate_counter_clockwise_90()   #rotate counter clockwise
        cells [index] = 1               #flip the value of the cell
        move_forward(int_direction)     #move forward
        
        
    

        


    
