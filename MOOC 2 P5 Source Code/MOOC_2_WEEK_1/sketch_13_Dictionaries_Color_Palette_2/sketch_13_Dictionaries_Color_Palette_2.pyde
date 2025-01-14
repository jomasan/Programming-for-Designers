# Canvas dimensions
image_size_x = 1200
image_size_y = 600

#create a dictionary
my_dict = {
           "Coral" : ["FFFFCAB1","FF69A2B0","FF659157","FFA1C084","FFE05263"],
           "Rusty" : ["FF9AD2CB","FFD7EBBA","FFFEFFBE","FFEBD494", "FF472836"],
           "Misty" : ["FF392F5A","FFF092DD","FFFFAFF0","FFEEC8E0", "FFA8C7BB"]
           }


#Access the data through the key
#print (my_dict ["Coral"][0] )
print (my_dict.get("Coral")[0] )

def setup():

    size(image_size_x, image_size_y) 
    
    #access an entry in the dictionay to use as a background color
    background( unhex(my_dict.get("Coral")[0] ) )


    
    
