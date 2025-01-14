#EXAMPLE OF A CLASS TO DRAW A GRADIENT RECTANGLE
import random

#In order to work with multiple files, we need to import the classes that have been defined in other scripts
import Gradient_Rectangle_Class as GR 
import Gradient_Circle_Class as GC

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#declare the class - and provide data for each argument
G_R_01 = GR.Gradient_Rectangle(
                            vec_position = PVector (50,100,0) , 
                            rec_size = 50,
                            vec_velocity = PVector (1,0,0),
                            color = color (0,0,255)
                            )
G_C_01 = GC.Gradient_Circle(
                            vec_position = PVector (75,200,0) , 
                            rec_size = 50,
                            vec_velocity = PVector (0.5,0,0),
                            color = color (0,255,0)
                            )

                          

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y)
    background(0,0,0)
    
def draw():
    #Now that we have a class created, we can call it's functions to execute it's code
    G_R_01.draw() 
    G_C_01.draw()

    G_R_01.move()
    G_C_01.move()
    
    


  








    
    
