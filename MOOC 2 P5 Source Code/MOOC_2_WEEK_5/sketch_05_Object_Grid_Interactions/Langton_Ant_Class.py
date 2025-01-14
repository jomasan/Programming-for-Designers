import random
#Definition of a class
import Grid_Data_Class as GD 


class Langton_Ant(object):
    #DocString
    '''Ant class that moves over the grid based on the data stored'''

    #Class attributes
    x = 10
    y = 10
    dir = 0

    #Constructor - arguments that are required to create an instance of this class
    def __init__(self, x, y, dir, grid_object): # constructor
        self.x = x 
        self.y = y  
        self.dir = dir
        self.grid_object = grid_object

    
    #Functions ------

    #Function run will be a 'dashboard' that will call all other classes that build the behavior of this class
    def run(self):
        self.draw_ant()
        self.ant_behavior()
        self.stay_within_bounds()

    def draw_ant(self):
        fill(255,0,0)
        x_coord = self.grid_object.index_coord_x(self.x) + (self.grid_object.cell_size_x() / 2 )
        y_coord = self.grid_object.index_coord_y(self.y) + (self.grid_object.cell_size_y() / 2 )
        rectMode(CENTER)
        rect(x_coord, y_coord, 10,10)

    def ant_behavior(self):
        #If Cell is white:
        if(self.grid_object.get_data_by_index(self.x,self.y) == 1): 
            self.rotate_clockwise_90()                                   #rotate clockwise
            self.grid_object.set_data_by_index(self.x,self.y, 0)         #flip the value of the cell
            self.move_forward(self.dir)                                  #move forward
        #If Cell is black
        elif (self.grid_object.get_data_by_index(self.x,self.y) == 0):
            self.rotate_counter_clockwise_90()                           #rotate counter clockwise
            self.grid_object.set_data_by_index(self.x,self.y, 1)         #flip the value of the cell
            self.move_forward(self.dir)                                  #move forward

    #Walker Functions
    #Move Forward - add or substract to the index position depending on the orientation of the walker
    def move_forward(self, dir):
        if(dir == 0):
            self.x += 1 #MOVE RIGHT
        elif(dir == 1):
            self.y += 1 #MOVE DOWN
        elif(dir == 2):
            self.x -= 1 #MOVE LEFT
        elif(dir == 3):
            self.y -= 1 #MOVE UP

    #Rotate clockwise - change the direction variable dependening or your current direction
    def rotate_clockwise_90(self):
        if self.dir == 0 :
            self.dir = 1
        elif self.dir == 1 :
            self.dir = 2
        elif self.dir == 2 :
            self.dir = 3
        elif self.dir == 3 :
            self.dir = 0

    #Rotate counter clockwise - change the direction variable dependening or your current direction
    def rotate_counter_clockwise_90(self):
        if self.dir == 0 :
            self.dir = 3
        elif(self.dir == 1):
            self.dir = 0
        elif(self.dir == 2):
            self.dir = 1
        elif(self.dir == 3):
            self.dir = 2
    
    def stay_within_bounds(self):
        #Stay within bounds - make sure that the index of the walker is within the bounds of the grid
        if self.x < 0 : self.x = self.grid_object.cols - 1
        if self.x >= self.grid_object.cols : self.x = 0
        if self.y < 0 : self.y = self.grid_object.rows -1
        if self.y >= self.grid_object.rows : self.y = 0
 
