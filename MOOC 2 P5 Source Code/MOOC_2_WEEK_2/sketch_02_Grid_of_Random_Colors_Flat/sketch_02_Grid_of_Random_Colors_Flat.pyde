#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#define the resolution of a grid
reso_x = 10
reso_y = 10

#Let's start with an empty list
my_color_list = []

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)

    #Let's create some counting variables
    int_current_x = 0
    int_current_y = 0

    #Define the size of a Cell by dividing the size of the screen by the resolution of the grid
    cell_size_x = image_size_x / reso_x
    cell_size_y = image_size_y / reso_y

    #We'll do a nested loop - one loop for our iteration in X and another for Y
    for i in range(0, reso_x * reso_y):
        
        #Define the position of a cell by the i and j iteration provided in the loop, multiplied by the size of the cell
        pos_x = (int_current_x * cell_size_x) 
        pos_y = (int_current_y * cell_size_y)

        #Define a random color for red, green and blue channels
        c_red = random.randrange(0,255)
        c_green = random.randrange(0,255)
        c_blue = random.randrange(0,255)

        #Let's store our color data in the list - random will always return a new number, but if we store it in a list, we can retrieve the information later if needed.
        my_color_list.append( (c_red, c_green, c_blue) )
        
        #draw a rectangle 
        noStroke()
        fill(c_red, c_green, c_blue)
        rect(pos_x, pos_y, cell_size_x, cell_size_y)

        #Let's update our count:
        #Each iteration of the loop we increase x by 1
        int_current_x += 1

        #If x becomes larger than the intended resolution in x, it returns back to 0, and y increases by 1
        if(int_current_x >= reso_x):
            int_current_x = 0
            int_current_y += 1

        


#def draw():

  








    
    
