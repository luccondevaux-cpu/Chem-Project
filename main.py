import turtle

#start stuff here:

Window = turtle.Screen()

#initializing information here:

class Particle:
    def __init__(self, mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle):
        self.turtle = turtle.Turtle()
        #mass in quectograms, 10^-30 grams
        coord = [self.x_coord, self.y_coord, self.z_coord]
        vel = [self.x_vel, self.y_vel, self.z_vel]

class Charged_Particle(Particle):
    def __init__(self, mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, charge, turtle):
        super().__init__(mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, charge, turtle)

class Proton(Charged_Particle):
    def __init__(self, mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle, charge):
        super().__init__(mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle, charge)
        self.charge = 1
        self.mass = 1,672,621.72

class Electron(Charged_Particle):
    def __init__(self, mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle, charge):
        super().__init__(mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle, charge)
        self.charge = -1
        self.mass = 910.9389699

class Neutron(Charged_Particle):
    def __init__(self, mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle):
        super().__init__(mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle)
        self.mass = 1674927.5

#main run here:

Window.exitonclick()
clicked = False
Window.onscreenclick(clicked != clicked)

while not clicked:
    #code here
    pass
