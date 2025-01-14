# Canvas dimensions
image_size_x = 1200
image_size_y = 600

def setup():
    # Create a canvas with the specified width and height
    size(image_size_x, image_size_y)

    # Set the background color to black
    background(0, 0, 0)
   
def draw():
    # Refresh the background to clear previous drawings
    background(0)
    
    # Define a static vector
    vec_1 = PVector(500, 0)
    
    # Define a dynamic vector that follows the mouse position
    vec_2 = PVector(mouseX, mouseY)
    
    # Define the starting position for the vectors in the middle of the canvas
    pos_1 = PVector(image_size_x / 2, image_size_y / 2)
    
    # Copy pos_1 to create two more positions
    pos_2 = pos_1.copy()
    pos_3 = vec_2.copy().sub(pos_1)
    
    # Adjust pos_2 and pos_3 to represent the ends of vec_1 and the mouse vector, respectively
    pos_2.add(vec_1)
    pos_3.add(pos_1)
    
    # Draw a white line representing vec_1
    stroke(255)
    line(pos_1.x, pos_1.y, pos_2.x, pos_2.y)
    
    # Draw a red line representing the vector to the mouse position
    stroke(255, 0, 0)
    line(pos_1.x, pos_1.y, vec_2.x, vec_2.y)

    # Calculate and normalize vectors based on pos_1 for the dot product calculation
    vec_calc_1 = pos_2.copy().sub(pos_1)
    vec_calc_2 = pos_3.copy().sub(pos_1)
    
    vec_calc_1.normalize()
    vec_calc_2.normalize()
    
    # Normalize vec_1 and vec_2 for demonstration, though they're not used further here
    vec_1.normalize()
    vec_2.normalize()
    
    # Calculate the dot product of the two vectors
    dot_product = vec_calc_1.dot(vec_calc_2)
    
    # Print the dot product to the console
    println(dot_product)
