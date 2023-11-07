#!/usr/bin/env python3

from utils.brick import Motor, TouchSensor, EV3ColorSensor, wait_ready_sensors
import time

#=-=-=-=-= Initialization of variables, motors and sensor =-=-=-=-=#
#Variables
color_array = ["purple", "blue", "green", "yellow", "orange", "red"]
#Motors
RIGHT_MOVEMENT_MOTOR = Motor('A')
LEFT_MOVEMENT_MOTOR = Motor('B')
RACK_MOTOR = Motor('C')
KICK_MOTOR = Morot('D')
#Sensors
EMERGENCY_TOUCH = TouchSensor(1)
RIGHT_COLOR_SENSOR = EV3ColorSensor(2)
RIGHT_COLOR_SENSOR = EV3ColorSensor(3)

wait_ready_sensors()

#=-=-=-=-=-=-=-=-=-=- Get coordinates of fire -=-=-=-=-=-=-=-=-=-=#
def inputCoordinate():
    global color_arrays
    coordArray = [] #The array containing all coordinates to fires
    
    # get the coordinates of the fires of from the user
    print("Input the coordinate of the fire using the following format:")
    print("xCoordinate,yCoordinate,color")
    print("Once you are done enter an empty feild \n")
    
    coordinate = input("Enter the coordinate: ")
    
    while coordinate != "":
        try:
            splitCoord = coordinate.split(",")
            xCoord = int(splitCoord[0])
            yCoord = int(splitCoord[1])
            color = splitCoord[2].lower()
            
            if xCoord > 3 or xCoord < 0 or yCoord > 3 or yCoord < 0:
                print("The coordinate given is not between 0,0 or 3,3")
            
            elif color not in color_array:
                print("The color given is not a valid color",color_array)
            
            else:
                coordArray.append([xCoord, yCoord, color])
                    
        except:
            print("coordinate were not in the correct format")
        
        coordinate = input("Enter the coordinate: ")
    
    return coordArray
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#=-=-=-=-=-=-=-=-=-=-=-=-=-= Main =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
coordinates_fire = inputCoordinate()
print(coordinates_fire)
