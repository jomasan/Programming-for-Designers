#create a dictionary
my_dict = {
           "Red" : color(255,0,0),
           "Green" : color(0,255,0),
           "Blue" : color(0,0,255)
           }

#Let's visualize the whole dictionary
print (my_dict)

#Access the data through the key
print (my_dict ["Green"] )

def setup():

    size(800, 800) 
    
    #access an entry in the dictionay to use as a background color
    background( my_dict ["Green"] )







    
    
