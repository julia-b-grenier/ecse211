#!/usr/bin/env python3

from utils.brick import Motor
import time


color_array = ["purple", "blue", "green", "yellow", "orange", "red"]

def executeSystem():
    global moving_flag
    global color_array
    
    selected_color = input("select color:")
    if(selected_color in color_array):
        position = color_array.index(selected_color) * 180
        MOTOR.set_position(position)
        time.sleep(0.1)
        moving_flag = False
    else:
        print("color not in the array")

#Used for debugging purposes
if __name__=='__main__':
    
    MOTOR = Motor('A')
    MOTOR.reset_position()
    
    print("started")
    
    MOTOR.set_limits(0,90);
    MOTOR.set_position(0)
    
    while(True):
        if(not MOTOR.is_moving()):
            executeSystem()
    
    reset_brick()
    exit()