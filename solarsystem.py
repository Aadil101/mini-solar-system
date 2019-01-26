#solarsystem.py
#Aadil Islam
#February 18, 2018

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 1000000         # real seconds per simulation second
PIXELS_PER_METER = 8 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)

# sun and planets with following parameters:
# (mass in kg, x in meters, y in meters, vx in m/s, vy in m/s, radius in pixels, r, g, b)

sun =     Body(1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)
mercury = Body(0.330e24,57.9e9, 0, 0, 47.4e3, 4, 0.64, 0.16, 0.16)
venus =   Body(4.87e24, 108.2e9, 0, 0, 35.0e3, 5, 1, 0.5, 0)
earth =   Body(5.9736e24, 149.6e9, 0, 0, 29.8e3, 5, 0, 0, 1)
mars =    Body(0.642e24, 227.9e9, 0, 0, 24.1e3, 4, 1, 0, 0)

#sun comes first in list to indicate it is the system's center
solar_system = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)
