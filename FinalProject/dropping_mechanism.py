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
    elif(selected_color == "push"):
        pushCube()
    else:
        print("color not in the array")
        
def pushCube():
    MOTOR_PUSH.set_position_relative(360)
    time.sleep(2)

#Used for debugging purposes
if __name__=='__main__':
    
    MOTOR = Motor('A')
    MOTOR_PUSH = Motor('D')
    MOTOR.reset_position()
    MOTOR_PUSH.reset_position()
    
    print("started")
    
    MOTOR.set_limits(0,90);
    MOTOR.set_position(0)
    
    MOTOR_PUSH.set_limits(100,180)
    MOTOR_PUSH.set_position(0)
    
    while(True):
        if(not MOTOR.is_moving()):
            executeSystem()
    
    reset_brick()
    exit()