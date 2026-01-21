from turtle import *

#start stuff here:

Window = turtle.Screen()

#initializing information here:

class Particle:
    def __init__(self, mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle):
        self.turtle = turtle.Turtle()
        #mass in quectograms, 10^-30 grams
        coord = [self.x_coord, self.y_coord, self.z_coord]
        vel = [self.x_vel, self.y_vel, self.z_vel]
    
    def change_vel_charge(charged_particle_list):
        for particle in charged_particle_list:
            for vect_num in range(len(coord)):
                vect_disp = coord[vect_num] - particle.coord[vect_num]
                if vect_disp != 0:
                    vel_change += (charge * particle.charge) / (vect_disp**2)
    
    def change_pos():
        for i in range(len(coord)):
            coord[i] += vel[i]


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
    def __init__(self, mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle, charge):
        super().__init__(mass, x_coord, y_coord, z_coord, x_vel, y_vel, z_vel, turtle, charge)
        self.charge = 0
        self.mass = 1674927.5

#main run here:

Window.exitonclick()

particle_list = []
charged_particle_list = []

particle_turtles = []
charged_particle_turtles = []

clicked = False
for particle in particle_list:
    particle_turtles.append(Turtle())

for particle in particle_list:
    if particle.charge != 0:
        charged_particle_list.append(particle)
        charged_particle_turtles.append(Turtle())

while not clicked:
    #code here
    for i in range(len(particle_list)):
        particle_list[i].change_vel_charge(charged_particle_list)
        #change_vel_nucl here
        particle_list[i].change_pos()
        #figure out how to compute x, y pos, how to change size for z pos


    Window.onscreenclick(clicked != clicked)
