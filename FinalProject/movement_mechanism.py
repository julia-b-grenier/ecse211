#!/usr/bin/env python3

"""
Version 1 - Implementation of moving the robot forward
Version 2 - Implementation of moving backward and rotate left and right
Version 3 - Add validation check before performing a new motor directive that the motor are done with the previous directive
"""

from utils.brick import wait_ready_sensors, Motor, EV3ColorSensor
import time
import color_sensor_validation

#=-=-=-=-=-=- Initialization of variables -=-=-=-=-=-=#
left_wheel = Motor('C')
right_wheel = Motor('B')
both_wheel = Motor(["C,B"])
POWER_LIMIT = 25
SPEED_LIMIT = 500

RW = 0.02 # wheel radius
RB = 0.1 # base radius
DISTTODEG = 180/(3.1416*RW) # Scale factor for distance
ORIENTTODEG = RB/RW # Scale factor for rotation

right_color_sensor = EV3ColorSensor(2)
left_color_sensor = EV3ColorSensor(3)


def initialize_motors(motor_left, motor_right, sensor_left, sensor_right):
    "Initialize the motors"
    left_wheel = motor_left
    right_wheel = motor_right
    both_wheel.set_port([motor_left.port, motor_right.port])

    left_color_sensor = sensor_left
    right_color_sensor = sensor_right

    try:
        left_wheel.set_limits(POWER_LIMIT, SPEED_LIMIT)
        right_wheel.set_limits(POWER_LIMIT, SPEED_LIMIT)
        both_wheel.set_limits(POWER_LIMIT, SPEED_LIMIT)
        
    except IOError as error:
        print(error)

#=-=-=-=-=-=-=-=-=-=- Movement functions -=-=-=-=-=-=-=-=-=-=#
def move_dist_fwd(dist):
    "Make the robot move forward"
    try:
        wait_for_the_motors_to_be_done()

        #left_wheel.set_position_relative(int(dist*DISTTODEG))
        #right_wheel.set_position_relative(int(dist*DISTTODEG))
        both_wheel.set_position_relative(int(dist*DISTTODEG))
        color_sensor_adjustment()
        print("moved forward")
    except BaseException as error:
        print(error)

def move_dist_bwd(dist):
    "Make the robot move backward"
    try:
        wait_for_the_motors_to_be_done()

        move_dist_fwd(-dist)
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

        rotate_right(-angle)
        print("rotated left")
        
    except BaseException as error:
        print(error)


#=-=-=-=-=-=-=-=-= Helper functions =-=-=-=-=-=-=-=-=#
def wait_for_the_motors_to_be_done():
    time.sleep(1)
    right_wheel.wait_is_moving(.5)
    left_wheel.wait_is_moving(.5)

def color_sensor_adjustment():
    left_count = 0
    right_count = 0
    while(right_wheel.is_moving() or left_wheel.is_moving()):
        left_color_reading = color_sensor_validation.collect_color_sensor_data(left_color_sensor)
        right_color_reading = color_sensor_validation.collect_color_sensor_data(right_color_sensor)

        if (left_color_reading == "blue" or left_color_reading == "red"):
            left_count+=1
        elif (right_color_reading == "blue" or right_color_reading == "red"):
            right_count+=1
    
    wait_for_the_motors_to_be_done()
    if ( left_count > 0 ):
        move_dist_bwd(.05)
        rotate_right(10)
        move_dist_fwd(.05)
    elif ( right_count > 0):
        move_dist_bwd(.05)
        rotate_left(10)
        move_dist_fwd(.5)
        


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