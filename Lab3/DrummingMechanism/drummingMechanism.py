#!/usr/bin/env python3

"""
Activate the drumming mechanism
"""

from utils.brick import TouchSensor, wait_ready_sensors
import brickpi3
import time


TOUCH_SENSOR = TouchSensor(1)
BRICKPI = brickpi3.BrickPi3() # Create BrickPi instance
LEFT_MOTOR = BRICKPI.PORT_A # Motor used for left rotation
RIGHT_MOTOR = BRICKPI.PORT_D # Motor used for right rotation
POWER_LIMIT = 80 # Power limit %
SPEED_LIMIT = 720 # Degrees / second max
ROTATION_DEGREE = 40
DELAY_TIME = 1

wait_ready_sensors() # Note: Touch sensors actually have no initialization time
    
def initializeMotors():
    "Initialized the motors"
    try:
        BRICKPI=brickpi3.BrickPi3()
        
        BRICKPI.offset_motor_encoder(LEFT_MOTOR, BRICKPI.get_motor_encoder(LEFT_MOTOR))
        BRICKPI.set_motor_limits(LEFT_MOTOR, POWER_LIMIT, SPEED_LIMIT)
        BRICKPI.set_motor_power(LEFT_MOTOR, 0)
        
        BRICKPI.offset_motor_encoder(RIGHT_MOTOR, BRICKPI.get_motor_encoder(RIGHT_MOTOR))
        BRICKPI.set_motor_limits(RIGHT_MOTOR, POWER_LIMIT, SPEED_LIMIT)
        BRICKPI.set_motor_power(RIGHT_MOTOR, 0)
    except IOError as error:
        print(error)

def start_drumming_on_button_released():
    "Start the drumming mechanism when the button is pressed and released"
    try:
        while not TOUCH_SENSOR.is_pressed() :
            pass  # do nothing while waiting for the first button press
        
        while TOUCH_SENSOR.is_pressed() :
            pass  # wait for the button to be released
        
        time.sleep(1)
        print("Touch sensor pressed")
        while ( not TOUCH_SENSOR.is_pressed() ):
            BRICKPI.set_motor_position_relative(LEFT_MOTOR, ROTATION_DEGREE)
            BRICKPI.set_motor_position_relative(RIGHT_MOTOR, ROTATION_DEGREE)
            time.sleep(DELAY_TIME)
            BRICKPI.set_motor_position_relative(LEFT_MOTOR, -ROTATION_DEGREE)
            BRICKPI.set_motor_position_relative(RIGHT_MOTOR, -ROTATION_DEGREE)
            time.sleep(DELAY_TIME)
                    
    except BaseException as error:  # capture all exceptions
        print(error)
        exit()


if __name__=='__main__':
    initializeMotors()
    start_drumming_on_button_released()

