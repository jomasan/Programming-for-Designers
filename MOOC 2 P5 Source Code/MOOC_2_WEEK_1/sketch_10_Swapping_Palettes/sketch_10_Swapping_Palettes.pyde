#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600



#Create an empty list
my_color_palettes = []

current_palette = 0

random_index = 0

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 
    
    background( unhex("FFE05263") )

    #Let's create a color pallete
    #create your own palette at: https://coolors.co/ffcab1-69a2b0-659157-a1c084-e05263

    #Create an empty list
    my_color_list = []

    #remember to add "FF" before the hex value obtained from the website - otherwise it will show up transparent
    my_color_list.append (  unhex("FFFFCAB1")  ) 
    my_color_list.append (  unhex("FF69A2B0")  )
    my_color_list.append (  unhex("FF659157")  )
    my_color_list.append (  unhex("FFA1C084")  )
    my_color_list.append (  unhex("FFE05263")  )

    #let's add the list of colors to another list that will contain all our palettes
    my_color_palettes.append (my_color_list)

    #Create an empty list
    my_color_list_2 = []

    #lets add specific colors to this new list
    my_color_list_2.append (  unhex("FF9AD2CB")  ) 
    my_color_list_2.append (  unhex("FFD7EBBA")  )
    my_color_list_2.append (  unhex("FFFEFFBE")  )
    my_color_list_2.append (  unhex("FFEBD494")  )
    my_color_list_2.append (  unhex("FF472836")  )

    #let's add the list of colors to another list that will contain all our palettes
    my_color_palettes.append (my_color_list_2)

    #Create an empty list
    my_color_list_3 = []

    #lets add specific colors to this new list
    my_color_list_3.append (  unhex("FF392F5A")  ) 
    my_color_list_3.append (  unhex("FFF092DD")  )
    my_color_list_3.append (  unhex("FFFFAFF0")  )
    my_color_list_3.append (  unhex("FFEEC8E0")  )
    my_color_list_3.append (  unhex("FFA8C7BB")  )

    #let's add the list of colors to another list that will contain all our palettes
    my_color_palettes.append (my_color_list_3)

def draw():
    
    #we'll execute some draing every third frame, in order to give it slow down the speed of the drawing
    if frameCount % 3 == 0:

        #create a random number within the length of colors in our palette
        random_index = random.randrange(0, len( my_color_palettes[current_palette] ) )

        #select a random entry from our color palette
        random_color_from_palette = my_color_palettes[current_palette] [random_index]

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

#here we will create some interactivity to restart the system when we press a key in the keyboard
def keyPressed():
    
    #first lets declare the variables that we will use in the function
    global current_palette, my_color_palettes

    #this will detect if we are pressing a key
    if keyPressed:
        print ("CALLED")
        #and now we can evaluate if we are pressing a specific key - in this case 'C', both capitalized or non-capitalized
        if key == 'c' or key == 'C':
            
            #once we press the key, we'll change the active palette
            current_palette += 1
            
            #and make sure that the index is not bigger than the number of elements un the list
            if(current_palette >= len(my_color_palettes)):
                current_palette = 0
            
            #finally we can reset the background color with the last color of the new palette active
            background( my_color_palettes[current_palette] [4] )







    
    
