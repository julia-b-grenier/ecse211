#!/usr/bin/env python3

"""
Version 1 - Implement moving the array of color to get a specific color
Version 2 - Implement the pushing cube function
"""

from utils.brick import Motor
import time

color_array = ["purple", "blue", "green", "yellow", "orange", "red"]

def initialize_motors():
    MOTOR = Motor('A')
    MOTOR_PUSH = Motor('D')
    MOTOR.reset_position()
    MOTOR_PUSH.reset_position()
    
    print("started")
    
    MOTOR.set_limits(0,90);
    MOTOR.set_position(0)
    
    MOTOR_PUSH.set_limits(100,180)
    MOTOR_PUSH.set_position(0)

def pushColor(selected_color, motor, motor_push):
    global color_array
    
    if(selected_color in color_array):
        position = color_array.index(selected_color) * 180
        motor.set_position(position)
        time.sleep(5)
        pushCube(motor_push)
    else:
        print("color not in the array")
        
def pushCube(motor_push):
    motor_push.set_position_relative(360)
    time.sleep(2)

#Used for debugging purposes
if __name__=='__main__':
    
    initialize_motors()
    
    while(True):
        if(not MOTOR.is_moving()):
            selected_color = input("select color:")
            pushColor(selected_color)
    
    reset_brick()
    exit()