#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600



def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) # create window: width, height

    #create a font
    f = createFont("Consolas", 24)
    textFont(f)
    textAlign(LEFT, CENTER)

def draw():
    # set background:  red, green, blue
    background(0,0,0)

    #define the text size
    textSize(16)

    #display a text in the screen at the coordinate specified
    text( "MY TEXT", 200,200)

    #define the text size
    textSize(48)

    #display a text in the screen at the coordinate specified
    text( "MY TEXT", 400,200)

    

    
    
