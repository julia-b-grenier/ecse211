#!/usr/bin/env python3

""" 
Version 1 - Determine the color from the reading of the color sensor by calculating the distance
"""

from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor, reset_brick
from time import sleep
import math

COLOR_SENSOR = EV3ColorSensor(4)
GREEN = [32,97,32, "Green"]
RED = [164,25,18, "Red"]
BLACK_OR_BLUE = [40, 30, 18, "Black"]
TABLE = [188,91,46, "Table"]
COLORS = [GREEN, RED, BLACK_OR_BLUE]

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.

data = []

def collect_color_sensor_data():
    "Collect color sensor data."
                
    CLICK = False;
    while ( True ):
        try:
            cs_data = COLOR_SENSOR.get_rgb()
            
            if cs_data is not None: # If None is given, then data collection failed that time
                print(cs_data)
                print(color_according_to_dist(cs_data))
                #if (cs_data[0] != 0 and cs_data[1] != 0 and cs_data[2]):
                    #data.append(cs_data)
                    
            sleep(0.5)
        except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
            
            exit()
            
def meanData():
    # Calculate the mean of the data
    mean = [0,0,0]
    for reading in data:
        mean[0] += reading[0]
        mean[1] += reading[1]
        mean[2] += reading[2]
        
    mean[0] = mean[0]/len(data)
    mean[1] = mean[1]/len(data)
    mean[2] = mean[2]/len(data)

def color_according_to_dist(reading):
    dist = math.sqrt((TABLE[0]-reading[0])**2+(TABLE[1]-reading[1])**2+(TABLE[2]-reading[2])**2)
    reading_color = "Table"
    for color in COLORS:
        new_dist = math.sqrt((color[0]-reading[0])**2+(color[1]-reading[1])**2+(color[2]-reading[2])**2)
        if new_dist < dist:
            reading_color = color[3]
            dist = new_dist
            
    return reading_color 
        
    

if __name__ == "__main__":
    collect_color_sensor_data()
    
    #print(color_according_to_dist([50,30,20]))
    
    reset_brick() # Turn off everything on the brick's hardware, and reset it

