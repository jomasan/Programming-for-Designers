import random
#Definition of a class

class Grid_Data(object):
    #DocString
    '''Grid Class that stores data in each node'''

    #Class attributes
    cols = 10
    rows = 10
    screen_width = 100
    screen_height = 100
    data = []

    #Constructor - arguments that are required to create an instance of this class
    def __init__(self, cols, rows, screen_width, screen_height): # constructor
        self.cols = cols 
        self.rows = rows  
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    #Functions ------

    #Function run will be a 'dashboard' that will call all other classes that build the behavior of this class
    def run(self):
        self.draw_grid_data()
    
    #Function to initialize the data
    def init_data(self):
        for i in range(0, self.cols):
            for j in range(0, self.rows):

                num = 0 #random.randint(0,1)
                self.data.append( num )
    

    #Draw the graphic in the screen
    def draw_grid_data(self):
        rec_size_x = self.screen_width / self.cols
        rec_size_y = self.screen_height / self.rows

        #Loop through the grid resolution and draw a rectangle based on the data
        for i in range(0, self.cols):
            for j in range(0, self.rows):

                #noStroke()
                stroke(0)
                #define the color of the rectangle based on the data stored in the list
                if(self.get_data_by_coord(i * rec_size_x, j * rec_size_y)) == 0:
                    fill(255)
                else:
                    fill(0) 
                #draw a rectangle in the location of the grid    
                rectMode(CORNER)          
                rect(i * rec_size_x, j * rec_size_y, rec_size_x,rec_size_y)
    

    #Helper function to collect the data in the list based on the coordinate x and y
    def get_data_by_coord(self, x_coord, y_coord):
        index = abs(   ( ( y_coord * self.rows ) / self.screen_height ) * self.cols + 
                       ( ( x_coord  * self.cols ) / self.screen_width)
                   )
        return self.data[index]
    
    def get_data_by_index(self, x_index, y_index):
        index = x_index + (y_index * self.cols)
        return self.data[index]
    
    def set_data_by_coord(self, x_coord, y_coord, value):
        index = abs(   ( ( y_coord * self.rows ) / self.screen_height ) * self.cols + 
                       ( ( x_coord  * self.cols ) / self.screen_width)
                   )
        self.data[index] = value
    
    def set_data_by_index(self, x_index, y_index, value):
        index = x_index + (y_index * self.cols)
        self.data[index] = value
    
    def index_coord_x (self, x):
        return x * (self.screen_width/self.cols)
    
    def index_coord_y (self, y):
        return y * (self.screen_height/self.rows)
    
    def cell_size_x (self):
        return (self.screen_width/self.cols)

    def cell_size_y (self):
        return (self.screen_height/self.rows)
    


                    

   
