"""_summary_
In this lesson, we will create a poly line.
    """

# Canvas dimensions
canvas_width = 1200
canvas_height = 600


def setup():
    # Create a canvas with the specifid width and height
    size(canvas_width, canvas_height)

    # Set the stroke weight
    strokeWeight(5)


def draw():
    # Set background color to black using the grayscale mothod.
    background(0)

    # Set stroke color to white using the grayscale mothod.
    stroke(255)
    
    # Set stroke weight 
    strokeWeight(2)
    
    #Define the fill for the shape
    fill(0,200,200,50)

    # Start the shape
    beginShape()
    
    # Define the points of the line as vertices
    vertex(250, 150)
    vertex(600, 200)
    vertex(400, 500)
    vertex(200, 400)
    
    #End the shape
    endShape(CLOSE)
