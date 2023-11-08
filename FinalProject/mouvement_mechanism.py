#!/usr/bin/env python3

from utils.brick import wait_ready_sensors, Motor
import brickpi3
import time

BRICKPI = brickpi3.BrickPi3()
LEFT_WHEEL = Motor('C')
RIGHT_WHEEL = Motor('B')
POWER_LIMIT = 25
SPEED_LIMIT = 500

RW = 0.02 # wheel radius
RB = 0.1 # base radius
DISTTODEG = 180/(3.1416*RW) # Scale factor for distance
ORIENTTODEG = RB/RW # Scale factor for rotation

def initialize_motors():
    "Initialize the motors"
    try:
        BRICKPI=brickpi3.BrickPi3()
        
        #LEFT_WHEEL.offset_encoder(BRICKPI.get_motor_encoder(LEFT_WHEEL))
        LEFT_WHEEL.set_limits(POWER_LIMIT, SPEED_LIMIT)
        #LEFT_WHEEL.set_power(0)
        
        #RIGHT_WHEEL.offset_encoder(BRICKPI.get_motor_encoder(RIGHT_WHEEL))
        RIGHT_WHEEL.set_limits(POWER_LIMIT, SPEED_LIMIT)
        #RIGHT_WHEEL.set_power(0)
    except IOError as error:
        print(error)

def move_dist_fwd(dist):
    "Make the robot move forward"
    try:
        LEFT_WHEEL.set_position_relative(int(dist*DISTTODEG))
        RIGHT_WHEEL.set_position_relative(int(dist*DISTTODEG))
        print("moved forward")
    except BaseException as error:
        print(error)

def move_dist_bwd(dist):
    "Make the robot move backward"
    try:
        
        LEFT_WHEEL.set_position_relative(int(-dist*DISTTODEG))
        RIGHT_WHEEL.set_position_relative(int(-dist*DISTTODEG))
        print("moved backward")
    except BaseException as error:
        print(error)

def rotate_right(angle):
    "Make the robot rotate right"
    try:
        LEFT_WHEEL.set_position_relative(int(angle*ORIENTTODEG))
        RIGHT_WHEEL.set_position_relative(int(-angle*ORIENTTODEG))
        print("rotated right")
    except BaseException as error:
        print(error)

def rotate_left(angle):
    "Make the robot rotate left"
    try:
        LEFT_WHEEL.set_position_relative(int(-angle*ORIENTTODEG))
        RIGHT_WHEEL.set_position_relative(int(angle*ORIENTTODEG))
        print("rotated left")
        
    except BaseException as error:
        print(error)

if __name__ == '__main__':
    print("started")
    initialize_motors()
    move_dist_fwd(0.3)
    time.sleep(5)
    rotate_right(90)
    time.sleep(3)
    move_dist_fwd(0.6)
    time.sleep(10)
    rotate_left(90)
    time.sleep(3)
    move_dist_fwd(-0.3)
    #move_dist_fwd(-0.3)
    #rotate_right(90)
    #rotate_left(90)
    #rotate_left(90)
    print("successful")