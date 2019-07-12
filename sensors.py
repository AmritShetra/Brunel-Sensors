# https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_sound_sensor.py

import time
import grovepi

# Connections
sound_sensor = 0 # Port A0
ultrasonic_ranger = 4 # Port D4
red_led = 5 # Port D5

grovepi.pinMode(sound_sensor, "INPUT")
grovepi.pinMode(red_led, "OUTPUT")

room_occupied = False

while True:
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
        else:
            grovepi.digitalWrite(red_led, 0)
        
        time.sleep(0.5)
    
    except IOError:
        print ("Error")

