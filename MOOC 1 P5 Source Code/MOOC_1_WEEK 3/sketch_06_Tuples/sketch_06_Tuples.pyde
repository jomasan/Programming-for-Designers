"""
Summary: This code demonstrates the creation of a tuple containing country names, 
iterating over it to print each country, and attempting to modify an element, 
which results in an error because tuples are immutable.
"""
import random

# Canvas dimensions
canvas_width = 1200
canvas_height = 600

def setup():
    # Create a canvas with the specified width and height
    size(canvas_width, canvas_height)

    # Set the background color to black
    background(0)

    # Set the stroke color to red
    stroke(255,0,0)
    
    # Let's create a tuple of countries
    countries = ("USA", "Canada", "Mexico")
    
    # Iterate over the tuple and print each element
    for i in countries:
        print(i)
        
    # Access and print the first element of the tuple
    print("First element: " + countries[0])
    
    # Attempt to modify the first element of the tuple to demonstrate that tuples are immutable, which will raise an error
    countries[0] = "Brazil"
    print(countries[0])
