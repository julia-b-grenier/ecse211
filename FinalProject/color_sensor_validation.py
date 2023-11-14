#!/usr/bin/env python3

""" 
Version 1 - Determine the color from the reading of the color sensor by calculating the distance
Version 2 - Add blue color and clean up functions so it can be called from main
"""

from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor, reset_brick
from time import sleep
import math

GREEN = [32,97,32, "green"]
RED = [164,25,18, "red"]
BLACK = [40, 30, 18, "black"]
BLUE = [50,50,60, "blue"] # put real blue value
TABLE = [188,91,46, "table"]
COLORS = [GREEN, RED, BLACK, BLUE]


def collect_color_sensor_data(color_sensor, result_array):
    try:
        cs_data = color_sensor.get_rgb()
        
        if cs_data is not None: # If None is given, then data collection failed that time
            return color_according_to_dist(cs_data)
                
        sleep(0.5)
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        exit()


def color_according_to_dist(reading):
    dist = math.sqrt((TABLE[0]-reading[0])**2+(TABLE[1]-reading[1])**2+(TABLE[2]-reading[2])**2)
    reading_color = "table"
    for color in COLORS:
        new_dist = math.sqrt((color[0]-reading[0])**2+(color[1]-reading[1])**2+(color[2]-reading[2])**2)
        if new_dist < dist:
            reading_color = color[3]
            dist = new_dist
            
    return reading_color
        
    

if __name__ == "__main__":
    color_sensor = EV3ColorSensor(4)
    wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.

    while( True ):
        print(collect_color_sensor_data(color_sensor))
    
    reset_brick() # Turn off everything on the brick's hardware, and reset it

