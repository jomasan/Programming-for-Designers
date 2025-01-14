#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#Create an empty list
my_color_list = []

random_index = 0

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 
    
    background( unhex("FFE05263") )

    #Let's create a color pallete
    #create your own palette at: https://coolors.co/ffcab1-69a2b0-659157-a1c084-e05263

    #remember to add "FF" before the hex value obtained from the website - otherwise it will show up transparent
    my_color_list.append (  unhex("FFFFCAB1")  ) 
    my_color_list.append (  unhex("FF69A2B0")  )
    my_color_list.append (  unhex("FF659157")  )
    my_color_list.append (  unhex("FFA1C084")  )
    my_color_list.append (  unhex("FFE05263")  )

def draw():

    if frameCount % 5 == 0:

        #create a random number within the length of colors in our palette
        random_index = random.randrange(0, len(my_color_list) )

        #select a random entry from our color palette
        random_color_from_palette = my_color_list [random_index]

        #define the style for our graphics 
        stroke(0,0,0)
        
        #use the random color from our palette as the color for our graphic
        fill( random_color_from_palette )

        #define a random location
        random_pos_x = random.randrange(0,image_size_x)
        random_pos_y = random.randrange(0,image_size_y)
        
        #define a random size within a range
        size = random.randrange(0,100)

        #draw a circle 
        ellipse(random_pos_x, random_pos_y, size, size)  







    
    
