# Canvas dimensions
image_size_x = 1200
image_size_y = 600

def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y) 
    
    #define a color using R,G,B 
    rgb_color = color(224, 82, 99)

    #convert the rgb color to hexadecimal
    hex_color = hex(rgb_color)

    #lets see the hex value of the color we generated
    print (hex_color)

    #background define by unhexing a hex color value
    background( unhex("FFE05263") )





    
    
