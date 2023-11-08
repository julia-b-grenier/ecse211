#!/usr/bin/env python3

from utils.brick import Motor, reset_brick
import time

MOTOR = Motor('D')


def pushCube():
    MOTOR.set_position_relative(360)
    time.sleep(1)

        
if __name__ == "__main__":
    MOTOR.reset_position()
    MOTOR.set_limits(100,360)
    
    pushCube()

    reset_brick()
    exit()
    
    