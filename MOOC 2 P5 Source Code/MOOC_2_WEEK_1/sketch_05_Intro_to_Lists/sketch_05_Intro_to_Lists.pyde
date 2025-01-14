#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#Create an empty list
my_list = []

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) # create window: width, height

    #Lets create a list with 100 random numbers
    for i in range(0,99):
        my_list.append ( random.randrange(0,255) )

    #print the list of number stored in the list
    print(my_list)

    
