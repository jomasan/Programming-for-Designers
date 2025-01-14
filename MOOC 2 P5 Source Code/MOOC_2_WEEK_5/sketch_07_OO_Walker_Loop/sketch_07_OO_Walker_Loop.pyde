import random

#In order to work with multiple files, we need to import the classes that have been defined in other scripts
import Discrete_Walker_Class as DW 

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#Initiate an empty list to store the class instances
D_W_List = []


def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y)

    # Create a black background
    background(0,0,0)

    #A for loop to create 20 instances of the class
    for i in range(0,20):

        #In this syntax, we will append to the list the instance of the class being created
        D_W_List.append (DW.Discrete_Walker(
                                    vec_position = PVector (i * 20,100,0) , 
                                    rec_size = 10,
                                    vec_velocity = PVector (1,0,0),
                                    r = 0,
                                    g = 0,
                                    b = 255,
                                    x_max = image_size_x,
                                    y_max = image_size_y
                                    )
                        ) 
    
def draw():

    #Run a for loop through each one of the class instances and execute the run function
    for i in range(0,20):
        D_W_List[i].run()
    
    


  








    
    
