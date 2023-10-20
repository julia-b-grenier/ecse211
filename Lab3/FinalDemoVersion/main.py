import drummingMechanism, fluteMechanism

from threading import Thread
from utils import sound
from utils.brick import wait_ready_sensors, EV3GyroSensor, TouchSensor, Motor, reset_brick                                                                                                                                                                                                                                                                                                                                                                                                                               
import time

DRUMMING_BUTTON = TouchSensor(1)
SOUND_BUTTON = TouchSensor(2)
GYRO_SENSOR = EV3GyroSensor(3)
EMERGENCY_BUTTON = TouchSensor(4)

IS_RUNNING = True

def initializeSystem():
    drummingMechanism.initializeMotors()
    wait_ready_sensors()
    
def thread_sound():
    while IS_RUNNING:
        fluteMechanism.executeSoundSystem(SOUND_BUTTON, GYRO_SENSOR)
        
def thread_drumming():
    drumming_activated = False
    while IS_RUNNING:
        if (DRUMMING_BUTTON.is_pressed()):
            drumming_activated = not drumming_activated
            
            while DRUMMING_BUTTON.is_pressed():
                pass
        
        if drumming_activated:
            print("drumming")
            drummingMechanism.executeDrummingSystem()
    
    
if __name__ == '__main__':
    initializeSystem()
    
    t_sound = Thread(target = thread_sound)
    t_drumming = Thread(target = thread_drumming)
    
    print("Start")
    t_sound.start()
    t_drumming.start()
    
    while ( not EMERGENCY_BUTTON.is_pressed() ):
        pass
    
    IS_RUNNING = False
    
    time.sleep(1)
    reset_brick()
    exit()
        
    

    
