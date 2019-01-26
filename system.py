#system.py
#Aadil Islam
#February 8, 2018

from cs1lib import *
from body import *

class System:

    # system constructor
    def __init__(self, body_list):

        # instantiate list of bodies
        self.body_list = body_list
        self.G = 6.67384e-11

    # acceleration for an orbiting body changes over time
    def compute_acceleration(self,i):

        # obviously acceleration for central body should be 0, so initialize as such
        ax = 0
        ay = 0

        # for ever orbiting body...
        for n in self.body_list:

            # ...but except for the central body itself...
            if n!=i:

                #compute new acceleration components ax and ay
                dx = n.x - i.x
                dy = n.y - i.y
                r = (dx**2+dy**2)**0.5
                a = self.G * n.mass / (r**2)
                ax = ax + a * dx/r
                ay = ay + a * dy/r

        return ax,ay

    # update movement for orbiting bodies
    def update(self, timestep):

        # for every orbiting body
        for i in self.body_list:

            # obtain new acceleration components
            (ax, ay) = self.compute_acceleration(i)

            # change velocity and position for body using the new acceleration
            i.update_velocity(timestep, ax, ay)
            i.update_position(timestep)

    # draw body objects
    def draw(self, cx, cy, pixels_per_meter):

        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx, cy, pixels_per_meter)




