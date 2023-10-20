#!/usr/bin/env python3

"""
Program that handles all the flute mechanics
"""

from utils import sound
from utils.brick import wait_ready_sensors, EV3GyroSensor, TouchSensor, reset_brick
import time

#An array of all the different sounds the flute can make
SOUNDS = [sound.Sound(duration=1.2, pitch="C5", volume=60), #pitch = 0 
          sound.Sound(duration=1.2, pitch="D5", volume=60), #pitch = 1
          sound.Sound(duration=1.2, pitch="E5", volume=60), #pitch = 2
          sound.Sound(duration=1.2, pitch="F5", volume=60), #pitch = 3
          sound.Sound(duration=1.2, pitch="G5", volume=60), #pitch = 4 (ORIGIN NOTE)
          sound.Sound(duration=1.2, pitch="A5", volume=60), #pitch = 5
          sound.Sound(duration=1.2, pitch="B5", volume=60), #pitch = 6
          sound.Sound(duration=1.2, pitch="C6", volume=60)] #pitch = 7 

# The function that reads if the sound button is pressed,
# and play the appropriate note depending on the gyro.
def executeSoundSystem(SOUND_BUTTON, GYRO_SENSOR):
    
    #This gets the current rotation and velocity of the current gyro sensor.
    mesure = GYRO_SENSOR.get_both_measure() 
    
    try:
        if(SOUND_BUTTON.is_pressed()): #Check if button is pressed
            if(mesure != None):
                angle = mesure[0] #Gets only the current rotation
                
                #start your pitch after a revolution, so you can also go backwards.
                #pitch = 4 is your origin (w/o offset). the +45 is just an offset.
                #Max backward you can go is 1, which is turned the opposite way to
                #a full revolution. Just angle/90 is pitch = 0
                pitch = int((angle+360+45)/90) 
                
                if(pitch >= 0 and pitch < len(SOUNDS)): #Checks if found pitch is in the range of the array `SOUNDS`
                    print(pitch) # Debug
                    SOUNDS[pitch].play()
                    SOUNDS[pitch].wait_done()
    except:
        print("Error in Flute System.")
    

# This is run for debug purposes only, this will only run the flute mechanisme on its own
if __name__=='__main__':
    
    print("started")
    EXIT_SENSOR = TouchSensor(4)
    SOUND_BUTTON = TouchSensor(2)
    GYRO_SENSOR = EV3GyroSensor(3)
    
    wait_ready_sensors()
    
    while(not EXIT_SENSOR.is_pressed()): #Continues the flute until EXIT button is pressed
        executeSoundSystem(SOUND_BUTTON, GYRO_SENSOR)
    
    reset_brick()
    exit()
    