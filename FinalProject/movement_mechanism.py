#!/usr/bin/env python3

"""
Version 1 - Implementation of moving the robot forward
Version 2 - Implementation of moving backward and rotate left and right
Version 3 - Add validation check before performing a new motor directive that the motor are done with the previous directive
"""

from utils.brick import Motor, EV3ColorSensor, reset_brick, wait_ready_sensors
import time
import color_sensor_validation

#=-=-=-=-=-=- Initialization of variables -=-=-=-=-=-=#
left_wheel = Motor('B')
right_wheel = Motor('A')
POWER_LIMIT = 20
SPEED_LIMIT = 500

RW = 0.02 # wheel radius
RB = 0.1 # base radius
DISTTODEG = 180/(3.14159265359*RW) # Scale factor for distance
ORIENTTODEG = RB/RW # Scale factor for rotation

right_color_sensor = EV3ColorSensor(4)
left_color_sensor = EV3ColorSensor(3)

#wait_ready_sensors(True)

def initialize_motors(motor_left, motor_right, sensor_left, sensor_right):
    "Initialize the motors"
    left_wheel = motor_left
    right_wheel = motor_right

    left_color_sensor = sensor_left
    right_color_sensor = sensor_right

    try:
        left_wheel.set_limits(POWER_LIMIT, SPEED_LIMIT)
        right_wheel.set_limits(POWER_LIMIT, SPEED_LIMIT)
        
    except IOError as error:
        print(error)

#=-=-=-=-=-=-=-=-=-=- Movement functions -=-=-=-=-=-=-=-=-=-=#
def move_dist_fwd(dist):
    "Make the robot move forward"
    try:
        wait_for_the_motors_to_be_done()
        print("start move")
        left_wheel.set_position_relative(int(dist*DISTTODEG))
        right_wheel.set_position_relative(int(dist*DISTTODEG))
        #both_wheel.set_position_relative(int(dist*DISTTODEG))
        #color_sensor_adjustment()
        print("finish moving")
    except BaseException as error:
        print("Error:" + str(error))

def move_dist_bwd(dist):
    "Make the robot move backward"
    try:
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
        rotate_right(-angle)
        
        print("rotated left")
        
    except BaseException as error:
        print(error)


#=-=-=-=-=-=-=-=-= Helper functions =-=-=-=-=-=-=-=-=#
def wait_for_the_motors_to_be_done():
    time.sleep(1)
    right_wheel.wait_is_stopped(.5)
    left_wheel.wait_is_stopped(.5)
    
    
"""
def color_sensor_adjustment():
    left_count = 0
    right_count = 0
    table_count = 0
    start_sensing = time.time()
    
    while(time.time() - start_sensing < 2):
        wait_ready_sensors()
    
        left_color_reading = color_sensor_validation.collect_color_sensor_data(left_color_sensor)
        right_color_reading = color_sensor_validation.collect_color_sensor_data(right_color_sensor)
        
        if (left_color_reading != "table" or right_color_reading != "table"):
            print("left: " + left_color_reading)
            print("right: " + right_color_reading)
            
                
        if (left_color_reading == "blue" and right_color_reading == "table" or
            left_color_reading == "red" and right_color_reading == "table"):
            rotate_left(10)
            
        elif (right_color_reading == "blue"  and left_color_reading == "table" or
              right_color_reading == "red"  and left_color_reading == "table"):
            rotate_right(10)
    
        
    print("color readings done: " + str(left_count) + str(right_count))
"""
    
def move_fwd(dist):
    total_dist_done = 0.0
    print(total_dist_done < dist)
    while (total_dist_done < dist):
        left_color_reading = color_sensor_validation.collect_color_sensor_data(left_color_sensor)
        right_color_reading = color_sensor_validation.collect_color_sensor_data(right_color_sensor)
        
        if ((left_color_reading == "table" and right_color_reading == "table") or
            (left_color_reading == "green" or right_color_reading == "green")):
            move_dist_fwd(0.02)
            total_dist_done+=0.02
            
            if (left_color_reading == "green" and right_color_reading == "green" and total_dist_done>dist-0.05):
                print("green")
                break
            
        if ((left_color_reading == "blue" and right_color_reading == "table") or
            (left_color_reading == "red" and right_color_reading == "table")):
            move_dist_bwd(.02)
            rotate_left(5)
            move_dist_fwd(.03)
            rotate_right(2)
            total_dist_done+=0.01
            
        elif ((right_color_reading == "blue"  and left_color_reading == "table") or
              (right_color_reading == "red"  and left_color_reading == "table")):
            move_dist_bwd(.02)
            rotate_right(5)
            move_dist_fwd(.03)
            rotate_left(2)
            total_dist_done+=0.01
        
    print(total_dist_done)

if __name__ == '__main__':
    print("started")
    initialize_motors(left_wheel, right_wheel, left_color_sensor, right_color_sensor)
    print("start moving")
    
    move_fwd(0.3)
    move_fwd(0.3)
    rotate_left(88)
    move_fwd(0.3)
    """
    move_dist_fwd(0.05)
    move_dist_fwd(0.05)
    move_dist_fwd(0.05)
    move_dist_fwd(0.05)
    move_dist_fwd(0.05)
    move_dist_fwd(0.05)
    move_dist_fwd(0.05)
    move_dist_fwd(0.05)
    """
    #rotate_left(90)
    #move_dist_fwd(0.3)
    #move_dist_fwd(-0.3)
    #rotate_right(90)
    #rotate_left(90)
    #rotate_left(90)
    print("successful")