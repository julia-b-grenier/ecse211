#!/usr/bin/env python3

"""
Version 1 - Implementation of moving the robot forward
Version 2 - Implementation of moving backward and rotate left and right
Version 3 - Add validation check before performing a new motor directive that the motor are done with the previous directive
"""

from utils.brick import wait_ready_sensors, Motor
import time

left_wheel = Motor('C')
right_wheel = Motor('B')
POWER_LIMIT = 25
SPEED_LIMIT = 500

RW = 0.02 # wheel radius
RB = 0.1 # base radius
DISTTODEG = 180/(3.1416*RW) # Scale factor for distance
ORIENTTODEG = RB/RW # Scale factor for rotation

def initialize_motors(motorLeft, motorRight):
    "Initialize the motors"
    left_wheel = motorLeft
    right_wheel = motorRight

    try:
        left_wheel.set_limits(POWER_LIMIT, SPEED_LIMIT)
        right_wheel.set_limits(POWER_LIMIT, SPEED_LIMIT)
        
    except IOError as error:
        print(error)

def move_dist_fwd(dist):
    "Make the robot move forward"
    try:
        wait_for_the_motors_to_be_done()

        left_wheel.set_position_relative(int(dist*DISTTODEG))
        right_wheel.set_position_relative(int(dist*DISTTODEG))
        print("moved forward")
    except BaseException as error:
        print(error)

def move_dist_bwd(dist):
    "Make the robot move backward"
    try:
        wait_for_the_motors_to_be_done()

        left_wheel.set_position_relative(int(-dist*DISTTODEG))
        right_wheel.set_position_relative(int(-dist*DISTTODEG))
        print("moved backward")
    except BaseException as error:
        print(error)

def rotate_right(angle):
    "Make the robot rotate right"
    try:
        wait_for_the_motors_to_be_done()

        left_wheel.set_position_relative(int(angle*ORIENTTODEG))
        right_wheel.set_position_relative(int(-angle*ORIENTTODEG))
        print("rotated right")
    except BaseException as error:
        print(error)

def rotate_left(angle):
    "Make the robot rotate left"
    try:
        wait_for_the_motors_to_be_done()

        left_wheel.set_position_relative(int(-angle*ORIENTTODEG))
        right_wheel.set_position_relative(int(angle*ORIENTTODEG))
        print("rotated left")
        
    except BaseException as error:
        print(error)


def wait_for_the_motors_to_be_done():
    time.sleep(1)
    right_wheel.wait_is_moving(.5)
    left_wheel.wait_is_moving(.5)

if __name__ == '__main__':
    print("started")
    initialize_motors(left_wheel, right_wheel)

    move_dist_fwd(0.3)
    rotate_right(90)
    move_dist_fwd(0.6)
    rotate_left(90)
    move_dist_fwd(-0.3)
    #move_dist_fwd(-0.3)
    #rotate_right(90)
    #rotate_left(90)
    #rotate_left(90)
    print("successful")