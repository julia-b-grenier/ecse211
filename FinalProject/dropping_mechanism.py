#!/usr/bin/env python3

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

def pushColor(selected_color):
    global color_array
    
    if(selected_color in color_array):
        position = color_array.index(selected_color) * 180
        MOTOR.set_position(position)
        time.sleep(5)
        pushCube()
    else:
        print("color not in the array")
        
def pushCube():
    MOTOR_PUSH.set_position_relative(360)
    time.sleep(2)

#Used for debugging purposes
if __name__=='__main__':
    
    initialize_motors()
    
    while(True):
        if(not MOTOR.is_moving()):
            selected_color = input("select color:")
            executeSystem(selected_color)
    
    reset_brick()
    exit()