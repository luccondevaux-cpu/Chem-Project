import turtle
import time

#start stuff here:
Window = turtle.Screen()

#initializing information here:

class Particle:
    def __init__(self, coord, vel):
        pass#mass in quectograms, 10^-30 grams
    
    def change_pos(self):
        for i in range(len(self.coord)):
            self.coord[i] += self.vel[i]


class Charged_Particle(Particle):
    def __init__(self, coord, vel):
        super().__init__(coord, vel)
    
    def change_vel_charge(self, particle_list):
        for particle in particle_list:
            for vect_num in range(len(self.coord)):
                vect_disp = self.coord[vect_num] - particle.coord[vect_num]
                if vect_disp != 0:
                    self.vel[vect_num] += (self.charge * particle.charge) / (vect_disp**2)


class Proton(Charged_Particle):
    def __init__(self, coord, vel):
        super().__init__(coord, vel)
        self.charge = 1
        self.mass = 1,672,621.72
        self.coord = coord
        self.vel = vel

class Electron(Charged_Particle):
    def __init__(self, coord, vel):
        super().__init__(coord, vel)
        self.charge = -1
        self.mass = 910.9389699
        self.coord = coord
        self.vel = vel

class Neutron(Charged_Particle):
    def __init__(self, coord, vel):
        super().__init__(coord, vel)
        self.charge = 0
        self.mass = 1674927.5
        self.coord = coord
        self.vel = vel

#main run here:

#Window.exitonclick()
print("1got here")

particle_list = [Proton(coord=[0, 0, 0], vel=[0, 0, 0]), Proton(coord=[100, 100, 0], vel=[0, 0, 0])]
print("2got here")

particle_turtles = []
print("3got here")

clicked = False
for i in range(len(particle_list)):
    particle_turtles.append(turtle.Turtle())
    #particle_turtles[i].up()
    particle_turtles[i].shape("circle")
    print("turtle added")
print("4got here")

seconds = 0

while seconds > 10:
    #code here
    print("5got here")
    time.sleep(1)
    seconds +=1
    for i in range(len(particle_list)):
        print("6got here")
        particle_list[i].change_vel_charge(particle_list)
        #change_vel_nucl here
        particle_list[i].change_pos()
        #figure out how to compute x, y pos, how to change size for z pos
        particle_turtles[i].goto(particle_list[i].coord[0], particle_list[i].coord[1])
        turtle.update()

print("tf")
turtle.mainloop()