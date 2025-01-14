# vehicle.py
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_speed(self):
        return self.speed
    
    def get_name(self):
        return self.name
