#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#define the resolution of a grid
reso_x = 100
reso_y = 50

#CELLS DATA - this list will store the data of each cell in the grid
cells = []

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)
    
    #Calculate the total number of cells
    total_cells = reso_x * reso_y

    #Populate the data of the list with a random integer, either 0 or 1
    for i in range(0,total_cells):
        cells.append ( random.randint(0,1) )

    #Define the size of a Cell by dividing the size of the screen by the resolution of the grid
    cell_size_x = image_size_x / reso_x
    cell_size_y = image_size_y / reso_y

    #Create local variables for x and y to create a flat grid in a single loop
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

    
