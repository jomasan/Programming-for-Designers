#import the random module
import random

# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#Create an empty list
my_list = []
random_index = 0

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 

    #Lets create a list with 100 random numbers
    for i in range(0,99):
        my_list.append ( random.randrange(0,255) )

    #create a font
    f = createFont("Consolas", 24)
    textFont(f)
    textAlign(LEFT, CENTER)

def draw():
    # set background:  red, green, blue
    background(0,0,0)

    #display a label
    text ( "My List Length is: ", 100, 120 )
    
    #calculate how long is the list
    list_length = len(my_list)    

    #convert the length of the list into a string              
    str_list_length = str( list_length )        

    #display the list length
    text ( str_list_length, 600, 120 )

    #display a label
    text ( "A Random number in the list is: ", 100, 170)

    #select a random number within the list
    random_entry = my_list [random_index]

    #convert that entry into a string
    str_random_entry = str(random_entry)

    #display the value of the random entry
    text ( str_random_entry, 600, 170)

    


    
    
