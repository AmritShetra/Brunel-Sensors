## Brunel Sensors
This is a project that uses a Raspberry Pi and GrovePi+ sensors to analyse user behaviour patterns in meeting rooms. The project was created by myself, Amrit Shetra, during a research internship that took place in July, at Brunel University London, supervised by Dr. Stasha Lauria.

### Requirements
* Raspberry Pi (I've used the 3B, but anything should work)
* GrovePi+ sensors (I've used the Starter Kit for Raspberry Pi)

### Using the project
* I've used [this guide](https://rsjazz.wordpress.com/2016/06/01/raspberry-pi-unleashed-setup-the-grovepi/) to set up my Raspberry Pi so that it can use the GrovePi+ sensors.
* Linux command "nano sensors.py" to edit the main file
* Note that you might need to add the relevant write permission using "sudo chmod a+w sensors.py".
* Linux command "sudo python sensors.py" to execute the main file's code - 'sudo' required as keyboard requires root privileges.
* Ctrl + C will trigger a 'KeyboardInterrupt' to stop the program once it is in operation.
