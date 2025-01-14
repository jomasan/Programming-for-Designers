#Definition of a class

class Gradient_Rectangle(object):
    #DocString
    '''Rectangle that shifts color in a gradient as it moves and bounces with adjacent rectangles'''

    #Class attributes
    vec_position = PVector (0,0,0)
    vec_velocity = PVector (1,0,0)
    rec_size = 10
    x_max = 0
    y_max = 0
    r = 255
    g = 255
    b = 255
    rchange = 0.1
    gchange = 4
    bchange = 1
    index = 0
    others_List = []

    draw_radius = 80

    #Constructor - arguments that are required to create an instance of this class
    def __init__(self, vec_position, rec_size, vec_velocity, x_max, y_max, index, others_List): # constructor
        self.vec_position = vec_position 
        self.rec_size = rec_size  
        self.vec_velocity = vec_velocity
        self.x_max = x_max
        self.y_max = y_max
        self.index = index
        self.others_List = others_List

    #Functions ------

    #Function run will be a 'dashboard' that will call all other classes that build the behavior of this class
    def run(self):
        self.draw()
        self.move()
        self.bounce_on_border()
        #self.bouce_color()
        self.line_to_others_in_range()
    
    #Draw the graphic in the screen
    def draw(self):
        noStroke()
        fill(self.r,self.g,self.b)
        rectMode(CENTER)
        rect(self.vec_position.x, self.vec_position.y, self.rec_size, self.rec_size)

        stroke(50,50,50)
        noFill()
        ellipseMode(CENTER)
        ellipse(self.vec_position.x, self.vec_position.y, self.draw_radius, self.draw_radius)

    #Move function based on velocity data
    def move(self):
        self.vec_position.add(self.vec_velocity)

    #Function to shift direction if we reach the edge of the screen
    def bounce_on_border(self):
        if(self.vec_position.x < 0): 
            self.vec_velocity.mult(-1)
        if(self.vec_position.x > self.x_max): 
            self.vec_velocity.mult(-1)
    
    #Function to shift the color of the rectangle over time
    def bouce_color(self):
        self.r += self.rchange
        self.g += self.gchange
        self.b += self.bchange

        if(self.r < 0) : self.rchange *= -1
        if(self.r > 255) : self.rchange *= -1
        if(self.g < 0) : self.gchange *= -1
        if(self.g > 255) : self.gchange *= -1
        if(self.b < 0) : self.bchange *= -1
        if(self.b > 255) : self.bchange *= -1
    
    #Function that allows the class to change direction if close to the neighbor above
    def line_to_others_in_range(self):
        for other in self.others_List:
            if(other != self):
                diff = PVector.sub(self.vec_position,other.vec_position)
                dist = diff.mag()
      
                if(dist < self.draw_radius):
                    stroke(255,255,255)
                    strokeWeight(0.5)
                    line(self.vec_position.x,self.vec_position.y, other.vec_position.x,other.vec_position.y)
                    
                    noFill()
                    ellipseMode(CENTER)
                    ellipse(self.vec_position.x, self.vec_position.y, self.rec_size *2, self.rec_size*2)
                    noStroke()

                    

   
