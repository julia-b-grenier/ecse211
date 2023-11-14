#!/usr/bin/env python3

"""
Version 1 - Implement asking the input and getting the path finding result
Version 2 - Implement the code that handles the list of actions
"""

from utils.brick import Motor, TouchSensor, EV3ColorSensor, wait_ready_sensors, reset_brick
import path_finding, movement_mechanism, dropping_mechanism
import time

#=-=-=-=-= Initialization of variables, motors and sensor =-=-=-=-=#
#Variables
color_array = ["purple", "blue", "green", "yellow", "orange", "red"]
#Motors
RIGHT_MOVEMENT_MOTOR = Motor('A')
LEFT_MOVEMENT_MOTOR = Motor('B')
RACK_MOTOR = Motor('C')
KICK_MOTOR = Motor('D')
#Sensors
EMERGENCY_TOUCH = TouchSensor(1)
RIGHT_COLOR_SENSOR = EV3ColorSensor(2)
LEFT_COLOR_SENSOR = EV3ColorSensor(3)

reset_brick()
dropping_mechanism.initialize_motors(RACK_MOTOR, KICK_MOTOR)
movement_mechanism.initialize_motors(LEFT_MOVEMENT_MOTOR, RIGHT_MOVEMENT_MOTOR, RIGHT_COLOR_SENSOR, LEFT_COLOR_SENSOR)
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
start = time.time()
print(coordinates_fire)
instructionList = path_finding.getInstructionList(coordinates_fire)
print(instructionList)

for instruction in instructionList:
    if instruction == "FWD":
        print("Action: FWD")
        movement_mechanism.move_dist_fwd(.3)

    elif instruction == "left":
        print("Action: left")
        movement_mechanism.rotate_left(90)

    elif instruction == "right":
        print("Action: right")
        movement_mechanism.rotate_right(90)

    elif instruction == "creepFWD":
        print("Action: creepFWD")
        movement_mechanism.move_dist_fwd(.22)

    elif instruction == "creepBWD":
        print("Action: creepBWD")
        movement_mechanism.move_dist_bwd(.22)

    elif instruction in color_array:
        dropping_mechanism.pushColor(instruction,RACK_MOTOR,KICK_MOTOR)

    else:
        print("INSTRUCTION NOT AN INSTRUCTION?")

end = time.time()

reset_brick()

print(end - start)
