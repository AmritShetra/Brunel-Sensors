## Brunel Sensors
This is a project that uses a Raspberry Pi and GrovePi+ sensors to analyse user behaviour patterns in meeting rooms. The project was created by myself, Amrit Shetra, during a research internship that took place in July, at Brunel University London, supervised by Dr. Stasha Lauria.
  
Prior to this project, I had no experience using a Pi and my Python knowledge was basic. During the project, I experienced many unexpected issues which meant that I constantly had to change my plan for what the code would do. Firstly, there were setbacks regarding the Camera module - the original one supplied to me did not work, meaning that I had to code using the sensors until I received a replacement. 

A couple of the sensors that I planned on using (Sound, etc.) did not function well, so I used one that did (Ultrasonic Ranger). This led to me designing a system that tracks when people walk past the sensor (so they have either entered or left the room) and trying to track statistics, which can then be put into a graph.

I encountered many issues regarding the installation of OpenCV on the Pi, usually resulting in the Pi freezing. Eventually, I was able to get it installed, using the guide linked below. 

This, however, meant that I lost all files on the Pi and essentially had it reset. Thanks to the powers of git, I cloned this repo and was free to continue working - hopefully, this time being able to use the Camera module in my work. Once again, I encountered errors with installing the necessary libraries (hopefully this is fixed by the presence of the "requirements.txt" file), and the sensors.py code seems to just malfunction.

### Requirements
* Raspberry Pi (I've used the 3B, but anything should work)
* GrovePi+ sensors (I've used the Starter Kit for Raspberry Pi)
* Pi Camera module

### Setup
* [This guide](https://www.pyimagesearch.com/2016/11/21/raspbian-opencv-pre-configured-and-pre-installed/) was used to set up the Raspberry Pi so that it already has Python 3 and OpenCV installed.
* I've used [this guide](https://rsjazz.wordpress.com/2016/06/01/raspberry-pi-unleashed-setup-the-grovepi/) to download the necessary software and drivers, so that it can use the GrovePi+ sensors.
* Use the command "curl -kL dexterindustries.com/update_grovepi | bash" to update the software.
* Use the command "pip install -r requirements.txt" to install the packages used in the project.
* When I installed packages, I usually had to use "sudo python -m pip install ___ " with __ being the package name.
* In the case of "matplotlib", there was a "MemoryError" which meant I had to use the command "sudo python -m pip --no-cache-dir install matplotlib".

### Using the project
* Each time you open a new terminal window, you should need to type "source ~/.profile" and "workon py3cv3" to access the virtual environment that holds Python3 and OpenCV - this is also mentioned in the first guide linked above!
* Linux command "sudo nano sensors.py" to edit the main file. Or if you'd like a GUI, try out "sudo thonny sensors.py".
* Note that you might need to add the relevant write permission using "sudo chmod a+w sensors.py".
* Linux command "sudo python sensors.py" to execute the main file's code - 'sudo' required as keyboard requires root privileges.
* Ctrl + C will trigger a 'KeyboardInterrupt' to stop the program once it is in operation.
