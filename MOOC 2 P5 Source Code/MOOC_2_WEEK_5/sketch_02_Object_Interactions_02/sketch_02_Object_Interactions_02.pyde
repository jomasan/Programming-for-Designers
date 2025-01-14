#EXAMPLE OF A CLASS TO DRAW A GRADIENT RECTANGLE
import random
import Gradient_Rectangle_Class as GR 

image_size_x = 1200
image_size_y = 600

myList = []
num_cols = 8

def setup():
    size(image_size_x, image_size_y) # create window: width, height
    background(0,0,0)

    for i in range(0,num_cols):
        #arguments for the constructor
        c_size = (image_size_y / num_cols) #size of the the rectangle
        c_pos_x = random.uniform(0,image_size_x)
        c_pos_y = (c_size * i) # position in y
        rand_speed = random.uniform(0.1,3) #random speed

        G_R_1 = GR.Gradient_Rectangle(vec_position = PVector (c_pos_x,c_pos_y,0) , 
                                      rec_size = c_size, 
                                      vec_velocity = PVector (rand_speed,0,0), 
                                      x_max = image_size_x,
                                      y_max = image_size_y,
                                      index = i,
                                      others_List = myList
                                      )
        myList.append(G_R_1)

   
def draw():
    for x in myList:
        x.run()
        

    


  








    
    
