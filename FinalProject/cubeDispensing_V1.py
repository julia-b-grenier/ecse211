#!/usr/bin/env python3

from utils import sound
from utils.brick import Motor
import time

MOTOR = Motor('A')
moving_flag = False
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
if __name__=='__main__':
    
    MOTOR.reset_position()
    
    print("started")
    
    MOTOR.set_limits(0,90);
    MOTOR.set_position(0)
    
    while(True):
        if(not MOTOR.is_moving()):
            executeSystem()
    
    reset_brick()
    exit()