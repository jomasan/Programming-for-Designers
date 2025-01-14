class Gradient_Rectangle(object):

    vec_position = PVector (0,0,0)
    vec_velocity = PVector (1,0,0)
    rec_size = 50
    x_max = 0
    y_max = 0
    r = 0
    g = 0
    b = 0
    rchange = 0.1
    gchange = 4
    bchange = 1
    index = 0
    others_List = []

    def __init__(self, vec_position, rec_size, vec_velocity, x_max, y_max, index, others_List): # constructor
        self.vec_position = vec_position 
        self.rec_size = rec_size  
        self.vec_velocity = vec_velocity
        self.x_max = x_max
        self.y_max = y_max
        self.index = index
        self.others_List = others_List
    
    def run(self):
        self.draw()
        self.move()
        self.bounce_on_border()
        self.bouce_color()
        self.bounce_with_each_other()
    
    def draw(self):
        noStroke()
        fill(self.r,self.g,self.b)
        rect(self.vec_position.x, self.vec_position.y, self.rec_size, self.rec_size)

    def move(self):
        self.vec_position.add(self.vec_velocity)

    def bounce_on_border(self):
        if(self.vec_position.x < 0): 
            self.vec_velocity.mult(-1)
        if(self.vec_position.x > self.x_max): 
            self.vec_velocity.mult(-1)
    
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
    
    def bounce_with_each_other(self):
        if(self.index > 0):
            other_up = self.others_List[self.index-1] #up
            dist = abs(self.vec_position.x - other_up.vec_position.x)
            if(dist < 2):
                self.vec_velocity.mult(-1)
                other_up.vec_velocity.mult(-1)
                self.r = 0
                self.g = 255
                self.b = 0

   
