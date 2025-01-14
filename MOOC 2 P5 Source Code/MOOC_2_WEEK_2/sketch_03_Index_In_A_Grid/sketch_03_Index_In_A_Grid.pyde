#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#define the resolution of a grid
reso_x = 100
reso_y = 50

#Let's start with an empty list - here we will store positions
my_pos_list = []

#Lets create a variable to store the size of a cell
cell_size_x = 0
cell_size_y = 0

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

            #Let's store a tuple with the position of x and y of each cell
            my_pos_list.append( (pos_x, pos_y) )
        
            #draw a rectangle 
            noStroke()
            fill(c_red, c_green, c_blue)
            rect(pos_x, pos_y, cell_size_x, cell_size_y)


def draw():

    #This if statement allows us to control the speed of the simulation - is optional
    if(frameCount % 1 == 0):

        #Define a random index within the bounds of the position list
        random_index = random.randrange(0,len(my_pos_list))
        
        #Recalculate the Cell size for the draw loop
        cell_size_x = image_size_x / reso_x
        cell_size_y = image_size_y / reso_y

        #draw a white rectangle in a random position obtaining the data from the list
        noStroke()
        #White
        fill(255, 255, 255)

        #The coordinates are defined by the random index, and later by the first or second element in the tuple, for x and y
        new_pos_x = my_pos_list[random_index][0]
        new_pos_y = my_pos_list[random_index][1]

        #Draw the rectangle
        rect(new_pos_x, new_pos_y, cell_size_x, cell_size_y)

        #Remove the used rectangle from the list - to avoid repetition
        del my_pos_list[random_index]

        #Check the size of the list - optional
        #print (len(my_pos_list))








    
    
