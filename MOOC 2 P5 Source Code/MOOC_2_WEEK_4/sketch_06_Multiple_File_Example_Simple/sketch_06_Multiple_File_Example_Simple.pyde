from vehicle import Vehicle  # Importing Vehicle class from vehicle.py

# Canvas dimensions
image_size_x = 1200
image_size_y = 600


def setup():
    # Create a canvas with the specifid width and height
    size(image_size_x, image_size_y)
    background(0,0,0)
    
    my_vehicle = Vehicle("Car", 120)
    
    println( my_vehicle.get_name() )
    println( my_vehicle.get_speed() )
    
    
    


  








    
    
