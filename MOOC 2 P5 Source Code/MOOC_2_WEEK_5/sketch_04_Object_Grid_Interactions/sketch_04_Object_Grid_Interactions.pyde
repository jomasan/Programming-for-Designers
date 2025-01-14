#EXAMPLE OF A CLASS TO DRAW A GRADIENT RECTANGLE
import random

#In order to work with multiple files, we need to import the classes that have been defined in other scripts
import Grid_Data_Class as GD 

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#Create one instance of the grid class and define the resolution of the grid
Main_Grid = GD.Grid_Data (  cols = 80,
                            rows = 40,
                            screen_width = image_size_x,
                            screen_height = image_size_y
                        ) 

def setup():

    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)

    #Initiate the data of the class
    Main_Grid.init_data()

   
def draw():

    # Create a black background
    background(0,0,0)

    #Execute the run function of the grid class
    Main_Grid.run()

    #Optional line to test if the index address is working
    #println(Main_Grid.get_data(mouseX, mouseY))
        

    


  








    
    
