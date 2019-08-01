## Brunel Sensors
This is a project that uses a Raspberry Pi and GrovePi+ sensors to analyse user behaviour patterns in meeting rooms. The project was created by myself, Amrit Shetra, during a research internship that took place in July, at Brunel University London, supervised by Dr. Stasha Lauria.

### Timeline
Prior to this project, I had no experience using a Pi and my Python knowledge was basic. During the project, I experienced many unexpected issues which meant that I constantly had to change my plan for what the code would do. Firstly, there were setbacks regarding the Camera module - the original one supplied to me did not work, meaning that I had to code using the sensors until I received a replacement. 

A couple of the sensors that I planned on using (Sound, etc.) did not function well, so I used one that did (Ultrasonic Ranger). This led to me designing a system that tracks when people walk past the sensor (so they have either entered or left the room) and trying to track statistics, which can then be put into a graph.

I encountered many issues regarding the installation of OpenCV on the Pi, usually resulting in the Pi freezing. Eventually, I was able to get it installed, using the guide linked below. 

This, however, meant that I lost all files on the Pi and essentially had it reset. Thanks to the powers of git, I cloned this repo and was free to continue working - hopefully, this time being able to use the Camera module in my work. Once again, I encountered errors with installing the necessary libraries (hopefully this is fixed by the presence of the "requirements.txt" file), and the sensors.py code seems to just malfunction.

I've used [this guide](https://www.pyimagesearch.com/2017/10/16/raspberry-pi-deep-learning-object-detection-with-opencv/) to get code that can detect objects through the Pi camera. It runs very slowly on the Pi, and eventually seems to overheat. It's able to accurately detect people, although it sometimes seems to detect sofas and bottles across the frame.

After getting that to work, I fixed sensors.py and data.py so that they work again, along with adding example code for making a pie chart (along with existing code I previously wrote to make a histogram) for data collected on the usage of the meeting rooms. This code works separately from the object detection code - the idea is that they could be merged so that the camera can be used to detect people, once movement is detected by the GrovePi sensor, but the sensor itself isn't the most accurate and I believe the Pi would overheat if the camera is used too much.

Finally, I was able to create a new file - "main.py" that combines most aspects of all the code developed, ensuring that if movement is detected, the camera is enabled and can detect people, with the occupancy data being recorded so that the user could analyse this.

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

### Files
* The 'main' file is designed to be sensors.py which can detect if there is movement in front of the GrovePi+'s Ultrasonic Ranger.
* This calls code from data.py and utilities.py. Data.py contains some sample code that shows how its methods can be easily used to create graphs.
* Camera.py can be used to test that the camera works - it will take a photo and can be exited through a key press.
* Real_time_object_detection.py contains the code for, well, detecting objects.

### Using the project
* Each time you open a new terminal window, you should need to type "source ~/.profile" and "workon py3cv3" to access the virtual environment that holds Python3 and OpenCV - this is also mentioned in the first guide linked above!
* Linux command "sudo nano ______.py" to edit a file. Or if you'd like a GUI, try out "sudo thonny ______.py".
* Note that you might need to add the relevant write permission using "sudo chmod a+w ______.py".
* Linux command "sudo python sensors.py" to execute the main file's code - 'sudo' required as keyboard requires root privileges.
* Ctrl + C will trigger a 'KeyboardInterrupt' to stop the program once it is in operation.
* Real_time_object_detection.py can be called using "python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel" and exited using a "q" key press.
* The main file can be called using the above command, but with a slight change - the name of the .py file must be changed to "main".

### Pie chart
Thanks for visiting the repository - I've added a screenshot of the pie chart I created, below. This shows how the data collected on the meeting rooms can be used by the Department of Computer Science. One idea I had involves tracking usage of the rooms across Monday-Friday - in the example below, you can see that Thursday's occupancy is much higher than the other days. In particular, Wednesday and Friday. Using this, we know that students should be advised to use the rooms on such days, hopefully therefore reducing congestion.
![Pie chart](https://i.imgur.com/Kb0AhGK.png)
