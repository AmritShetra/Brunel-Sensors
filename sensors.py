# https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_sound_sensor.py

import time
import grovepi
import numpy as np
import matplotlib as plt
from datetime import datetime
import keyboard

# Connections
sound_sensor = 0 # Port A0
ultrasonic_ranger = 4 # Port D4
red_led = 5 # Port D5

grovepi.pinMode(sound_sensor, "INPUT")
grovepi.pinMode(red_led, "OUTPUT")

program_active = True
room_occupied = False
printed = False # Check if datetime already printed while occupied
datetimes_when_occupied = []

def add_datetimes_to_list():
    ''' Adds the date and time when the room is occupied to a
        dictionary, which is added to a list containing each dictionary. '''
    now = datetime.now()
    print(now)
    d = {}
    d['time'] = now.time()
    d['day'] = now.strftime("%A")
    d['date'] = now.strftime("%d")
    d['month'] = now.strftime("%B")
    datetimes_when_occupied.append(d)

while program_active:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)
        
        # Read the distance
        distance_value = grovepi.ultrasonicRead(ultrasonic_ranger)
        
        # Printing values, mainly for testing purposes
        print (distance_value)
        print ("Sound sensor value = %d" %sensor_value)
        
        if distance_value < 500:
            room_occupied = not room_occupied
        
        if room_occupied:
            grovepi.digitalWrite(red_led, 1)
            print ("Room is occupied")
            if printed == False:
                add_datetimes_to_list()
                printed = True
        else:
            grovepi.digitalWrite(red_led, 0)
            printed = False
        
        time.sleep(0.5)
        
        if keyboard.is_pressed("C"):
            program_active = False

    except IOError:
        print ("Error")

# Exit the loop when prompted by the user
print("Program terminated")

# Print the contents of each dictionary from the list
for datetimes in datetimes_when_occupied:
    print(datetimes['time'])
    print(datetimes['day'])
    print(datetimes['date'])
    print(datetimes['month'])
