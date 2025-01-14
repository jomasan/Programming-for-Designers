"""_summary_
In this lesson, we draw the vertices of a poly line using a loop
    """

# Canvas dimensions
canvas_width = 1200  # Set the width for the drawing canvas
canvas_height = 600  # Set the height for the drawing canvas

def setup():
    # Initialize the canvas with the specified dimensions. This setup runs once at the beginning.
    size(canvas_width, canvas_height)

def draw():
    # Fill the canvas with a black background. This is done each time the draw function runs.
    background(0)
    
    # Set the color of the line (stroke) to white for drawing the polyline and points.
    stroke(255)
    # Disable filling shapes to only draw the outline of the polyline.
    noFill()
    
    # Initialize variables to control the shape of the sine wave.
    wavelength = 30  # Distance between wave peaks
    amplitude = 100  # Height of the wave from center to peak
    offset = 300     # Vertical offset of the wave from the top of the canvas
    
    # Calculate the frequency of the wave based on its wavelength.
    frequency = TWO_PI / wavelength
    
    # Begin drawing a complex, continuous shape (polyline).
    beginShape()
    
    # Loop through a range to calculate and draw each vertex of the curve.
    for i in range(0, 50):
        # Calculate the y-coordinate of the vertex using a sine function for a wave-like pattern.
        y = amplitude * sin(frequency * i) + offset
        # Calculate the x-coordinate of the vertex, spacing each point evenly.
        x = i * 20
        
        # Add a vertex to the shape at the calculated coordinates.
        vertex(x, y)
        
        # Temporarily increase the stroke weight to visually emphasize the vertex.
        strokeWeight(5)
        # Draw a point at the vertex location for visual emphasis.
        point(x, y)
        # Reset the stroke weight to a finer line for connecting vertices in the polyline.
        strokeWeight(1)
    
    # Finish drawing the polyline. This connects all the vertices defined by vertex() calls.
    endShape()

        
        
        
        
