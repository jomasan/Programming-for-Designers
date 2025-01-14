#EXAMPLE OF A CLASS TO DRAW A GRADIENT RECTANGLE
import random

#In order to work with multiple files, we need to import the classes that have been defined in other scripts
import Gradient_Rectangle_Class as GR 

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

# Initiate an empty list
myList = []

#variable for the number of columns 
num_cols = 40

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    # Create a black background
    background(0,0,0)

    #Let's execute a for loop through the number of columns we specified
    for i in range(0,num_cols):

        #arguments for the constructor
        c_size = (image_size_y / num_cols) #size of the the rectangle
        c_pos_x = random.uniform(0,image_size_x)
        c_pos_y = (c_size * i) # position in y
        rand_speed = random.uniform(-2,2) #random speed

        #Generate an instance of the class
        G_R_1 = GR.Gradient_Rectangle(vec_position = PVector (c_pos_x,c_pos_y,0) , 
                                      rec_size = c_size, 
                                      vec_velocity = PVector (rand_speed,0,0), 
                                      x_max = image_size_x,
                                      y_max = image_size_y
                                      )

        #finally, add the instance of the class to the list
        myList.append(G_R_1)

   
def draw():
    #Do a loop through all instances of the class that are stored in the list, and execute it's run function
    for x in myList:
        x.run()
        

    


  








    
    
