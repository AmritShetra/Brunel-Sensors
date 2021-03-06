# https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_sound_sensor.py

import time
import grovepi
import keyboard

# Import other Python files
import data
import utilities as utils

# Connections
ultrasonic_ranger = 4 # Port D4
red_led = 5 # Port D5

grovepi.pinMode(red_led, "OUTPUT")

program_active = True
room_occupied = False
printed = False # Check if datetime already printed while occupied
datetimes_when_occupied = []

while program_active:
    try:
        # Read the distance
        distance_value = grovepi.ultrasonicRead(ultrasonic_ranger)
        
        # Printing values, mainly for testing purposes
        print (distance_value)
        
        if distance_value < 500:
            room_occupied = not room_occupied
        
        if room_occupied:
            grovepi.digitalWrite(red_led, 1)
            print ("Room is occupied")
            if printed == False:
                utils.add_datetimes_to_list(datetimes_when_occupied)
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
utils.print_list(datetimes_when_occupied)
