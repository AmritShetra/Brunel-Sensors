# https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_sound_sensor.py

import time
import grovepi

# Connections
sound_sensor = 0 # Port A0

grovepi.pinMode(sound_sensor, "INPUT")

while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)
        
        print ("Sound sensor value = %d" %sensor_value)
        time.sleep(0.5)
    
    except IOError:
        print ("Error")


