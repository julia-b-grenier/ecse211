#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor, reset_brick
from time import sleep

COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(4)
TOUCH_SENSOR = TouchSensor(1)
EXIT_BUTTON = TouchSensor(2)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    "Collect color sensor data."
    "Collect continuous data from the ultrasonic sensor between two button presses."
                
    CLICK = False;
    output_file = open(COLOR_SENSOR_DATA_FILE, "w")
    while ( True ):
        try:
            if ( TOUCH_SENSOR.is_pressed() and not CLICK):
                
                CLICK = True
                print("Touch sensor pressed")
                
                cs_data = COLOR_SENSOR.get_rgb()            
                
                if cs_data is not None: # If None is given, then data collection failed that time
                    print(cs_data)
                    output_file.write(f"{cs_data}\n")
            
            elif ( not TOUCH_SENSOR.is_pressed() and CLICK):
                CLICK = False
            if ( EXIT_BUTTON.is_pressed() ):
                print("exit and save")
                output_file.close()
                reset_brick() # Turn off everything on the brick's hardware, and reset it
                exit()
        except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
            exit()


if __name__ == "__main__":
    collect_color_sensor_data()
