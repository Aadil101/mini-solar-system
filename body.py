#body.py
#Aadil Islam
#February 8, 2018

from cs1lib import *

class Body:

    # body constructor
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):

        self.mass = mass

        # for body movement
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        # for drawing body
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):

        # new_x = initial_x + velocity * time
        self.x = self.x + timestep * self.vx
        self.y = self.y + timestep * self.vy

    def update_velocity(self, timestep, ax, ay):

        # new_velocity = initial_velocity + acceleration * time
        self.vx = self.vx + timestep*ax
        self.vy = self.vy + timestep*ay

    def draw(self, cx, cy, pixels_per_meter):

        # paintbrush and paint for body
        disable_stroke()
        set_fill_color(self.r, self.g, self.b)

        # body's coordinates originate not from (0,0) but from (200,200) --> (cx,cy)
        # instance variables x and y describe deviation away from this new origin
        # but x and y are two large! must convert via multiplying by pixels_per_meter
        draw_circle(cx + self.x * pixels_per_meter, cy + self.y * pixels_per_meter, self.pixel_radius)


