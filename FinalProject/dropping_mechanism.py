#!/usr/bin/env python3

"""
Version 1 - Implement moving the array of color to get a specific color
Version 2 - Implement the pushing cube function
"""

from utils.brick import Motor
import time

color_array = ["purple", "blue", "green", "yellow", "orange", "red"]

#=-=-=-=-=-=- Initialization of variables -=-=-=-=-=-=#
def initialize_motors(motor, motor_push):
    motor.reset_position()
    motor_push.reset_position()
    
    motor.set_limits(0,90);
    motor.set_position(0)
    
    motor_push.set_limits(100,180)
    motor_push.set_position(0)
    
    print("Movement motors are initialized")

#=-=-=-=-= Cube dispenser functions =-=-=-=-=#
def pushColor(selected_color, motor, motor_push):
    global color_array
    
    if(selected_color in color_array):
        position = color_array.index(selected_color) * 180
        motor.set_position(position)
        time.sleep(1)
        motor.wait_is_stopped(1)
        pushCube(motor_push)
    else:
        print("color not in the array")
        
def pushCube(motor_push):
    motor_push.set_position_relative(-360)
    time.sleep(1)
    motor_push.wait_is_stopped(2)

#Used for debugging purposes
if __name__=='__main__':
    motor = Motor('A')
    motor_push = Motor('D')
    
    initialize_motors(motor, motor_push)
    
    while(True):
        if(not motor.is_moving()):
            selected_color = input("select color:")
            pushColor(selected_color,motor,motor_push)
    
    reset_brick()
    
    exit()