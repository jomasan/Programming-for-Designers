#EXAMPLE OF A CLASS TO DRAW A GRADIENT RECTANGLE
import random

#In order to work with multiple files, we need to import the classes that have been defined in other scripts
import Discrete_Walker_Class as DW 

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#create 3 instances of the class - providing different arguments for each
D_W_01 = DW.Discrete_Walker(
                            vec_position = PVector (50,100,0) , 
                            rec_size = 70,
                            vec_velocity = PVector (1,0,0),
                            r = 0,
                            g = 0,
                            b = 255,
                            x_max = image_size_x,
                            y_max = image_size_y
                            )

D_W_02 = DW.Discrete_Walker(
                            vec_position = PVector (800,400,0) , 
                            rec_size = 30,
                            vec_velocity = PVector (1,0,0),
                            r = 0,
                            g = 255,
                            b = 255,
                            x_max = image_size_x,
                            y_max = image_size_y
                            )

D_W_03 = DW.Discrete_Walker(
                            vec_position = PVector (500,300,0) , 
                            rec_size = 5,
                            vec_velocity = PVector (1,0,0),
                            r = 255,
                            g = 255,
                            b = 255,
                            x_max = image_size_x,
                            y_max = image_size_y
                            )

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)
    
def draw():
    #background(0,0,0)

    #Execute the run function of each one of the instances of the class
    D_W_01.run()
    D_W_02.run()
    D_W_03.run()
    
    


  








    
    
