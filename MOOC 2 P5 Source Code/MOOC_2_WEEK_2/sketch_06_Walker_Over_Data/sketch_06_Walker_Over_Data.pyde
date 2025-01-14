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

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y)

    # Create a black background
    background(0,0,0)
    
    #Calculate the total number of cells
    total_cells = reso_x * reso_y

    #Populate the data of the list with a random integer, either 0 or 1
    for i in range(0,total_cells):
        cells.append ( random.randint(0,0) )

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

        #increase the x coordinate by +1 or -1 at random
        int_current_index_x += random.randint(-1,1)
        #increase the y coordinate by +1 or -1 at random
        int_current_index_y += random.randint(-1,1)

        #Stay within bounds - make sure that the index of the walker is within the bounds of the grid
        if int_current_index_x < 0 : int_current_index_x = 0
        if int_current_index_x >= reso_x : int_current_index_x = reso_x -1
        if int_current_index_y < 0 : int_current_index_y = 0
        if int_current_index_y >= reso_y : int_current_index_y = reso_y -1

        #Convert X and Y coordinates into the index of a flat list
        index = int_current_index_x + (int_current_index_y * reso_x)

        #--------Optional: Debuging tips to check that this operation is working well
        #print ("x :"  + str(int_current_index_x) + ", " + "y: " + str(int_current_index_y))
        #print ("index :"  + str(index) )
        #print ("count :"  + str(count) )
        
        #The walker will be able to alter the data of the grid, from 0 to 1 and vice versa
        if(cells [index] == 0): 
            cells [index] = 1
        elif (cells [index] == 1):
            cells [index] = 0
        
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
