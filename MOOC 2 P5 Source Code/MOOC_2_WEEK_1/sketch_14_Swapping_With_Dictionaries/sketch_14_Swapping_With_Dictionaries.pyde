#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#create a dictionary
my_color_palettes = {
           "Coral" : ["FFFFCAB1","FF69A2B0","FF659157","FFA1C084","FFE05263"],
           "Rusty" : ["FF9AD2CB","FFD7EBBA","FFFEFFBE","FFEBD494", "FF472836"],
           "Misty" : ["FF392F5A","FFF092DD","FFFFAFF0","FFEEC8E0", "FFA8C7BB"]
           }

#Create an empty list
possible_characters = ['X','O','_','@']

current_palette = "Coral"

random_index = 0

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 
    
    #access an entry in the dictionay to use as a background color
    background( unhex( my_color_palettes.get("Coral")[0] ) )


def draw():
    
    #we'll execute some draing every third frame, in order to give it slow down the speed of the drawing
    if frameCount % 1 == 0:

        #create a random number within the length of colors in our palette
        random_index = random.randrange(0, len( my_color_palettes[current_palette] )-1 )
        
        #select a random entry from our color palette
        random_color_from_palette = my_color_palettes.get(current_palette)[random_index]

        #define the style for our graphics 
        stroke(0,0,0)
        
        #use the random color from our palette as the color for our graphic
        fill( unhex(random_color_from_palette) )
        
        #define a random location
        random_pos_x = random.randrange(0,image_size_x)
        random_pos_y = random.randrange(0,image_size_y)
        
        size = random.randrange(0,100)
        
        #draw a circle 
        ellipse(random_pos_x, random_pos_y, size, size)  
        
#here we will create some interactivity to restart the system when we press a key in the keyboard
def keyPressed():
    #first lets declare the variables that we will use in the function
    global current_palette, my_color_palettes

    #this will detect if we are pressing a key
    if keyPressed:
        #and now we can evaluate if we are pressing a specific key - in this case 'C', both capitalized or non-capitalized
        if key == 'c' or key == 'C':
            current_palette = "Coral"
            background( unhex( my_color_palettes.get(current_palette)[0] ) )
        if key == 'v' or key == 'V':
            current_palette = "Rusty"
            background( unhex( my_color_palettes.get(current_palette)[0] ) )
        if key == 'b' or key == 'B':
            current_palette = "Misty"
            background( unhex( my_color_palettes.get(current_palette)[0] ) )



    
    
