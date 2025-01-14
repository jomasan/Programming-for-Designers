#EXAMPLE OF A CLASS TO DRAW A GRADIENT RECTANGLE
import random

#In order to work with multiple files, we need to import the classes that have been defined in other scripts
import Grid_Data_Class as GD 
import Langton_Ant_Class as LA

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#Create one instance of the grid class and define the resolution of the grid
Main_Grid = GD.Grid_Data (  cols = 120,
                            rows = 60,
                            screen_width = image_size_x,
                            screen_height = image_size_y
                        ) 
Ant_1 = LA.Langton_Ant( x = 10,
                        y = 10,
                        dir = 1,
                        grid_object = Main_Grid
                        )
Ant_2 = LA.Langton_Ant( x = 50,
                        y = 20,
                        dir = 1,
                        grid_object = Main_Grid
                        )
Ant_3 = LA.Langton_Ant( x = 70,
                        y = 30,
                        dir = 1,
                        grid_object = Main_Grid
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
    Ant_1.run()
    Ant_2.run()
    Ant_3.run()

    #Optional line to test if the index address is working
    #println(Main_Grid.get_data(mouseX, mouseY))
        

    


  








    
    
