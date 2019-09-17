## Brunel Sensors
This is a project that uses a Raspberry Pi and GrovePi+ sensors to analyse user behaviour patterns in meeting rooms. The project was created by myself, Amrit Shetra, during a research internship that took place in July, at Brunel University London, supervised by Dr. Stasha Lauria.

### Timeline
Prior to this project, my experience using a Pi and coding in Python was minimal. During the project, I encountered many unexpected issues which meant I constantly had to change what the program would do. Firstly, there were setbacks regarding the Camera module - the original one supplied did not work, so I used only the GrovePi sensors until a replacement was provided.

Some of the sensors that I planned to use (Sound, etc.) did not function well so I used one that did (Ultrasonic Ranger). This led to me designing a system that tracks movement in front of the sensor (thus, entering/leaving the room) and recorded statistics, which could then be put into a graph.

There were many issues with installing OpenCV on the Pi, usually resulting in the Pi freezing. Nonetheless, I eventually installed it, using the guide below - this did wipe my data, though. Thanks to the powers of Git, I retrieved my repo and continued working. 

I encountered many issues regarding the installation of OpenCV on the Pi, usually resulting in the Pi freezing. Eventually, I was able to get it installed, using [this guide](https://www.pyimagesearch.com/2017/10/16/raspberry-pi-deep-learning-object-detection-with-opencv/). A lot of my code did somehow break, but I believe it's fixed.

The above link provided a way to detect objects through the Pi camera. It runs very slowly on the Pi, and eventually overheats. It accurately detects people (usually) but also throws in the odd sofa and bottle across the frame. Not a huge issue, but also not ideal - the overheating, however, is a problem...

I fixed sensors.py and data.py and added example code for making a pie chart and histogram. I used sample data on usage of the meeting rooms. This code works seperately from the object detection code, but could be merged in the future. However, the Ultrasonic Ranger is very sensitive and thus, not wholly accurate.

Finally, I combined most aspects of the code developed into main.py, where if movement is detected, the camera is enabled and detects people. The occupany data is recorded so the user could analyse this - currently, it is wiped when the program shuts down. A long-term solution that I did not have time to explore was to store this in a file and read it on program entry.

### Requirements
* Raspberry Pi (I've used the 3B, but anything should work)
* GrovePi+ sensors (I've used the Starter Kit for Raspberry Pi)
* Pi Camera module

### Setup
* [Guide on pre-configured Pi with Python3 and OpenCV installed](https://www.pyimagesearch.com/2016/11/21/raspbian-opencv-pre-configured-and-pre-installed/).
* [Guide on downloading necessary software and drivers so the Pi can use the GrovePi+ sensors.](https://rsjazz.wordpress.com/2016/06/01/raspberry-pi-unleashed-setup-the-grovepi/).
* Update the GrovePi+ software:
```
curl -kL dexterindustries.com/update_grovepi | bash
```
* Install the packages used in the project into the virtual environment:
```
pip install -r requirements.txt
```
* When I installed packages seperately, I had to use this (with ___ being the package name):
```
sudo python -m pip install ___ 
```
* In the case of "matplotlib", there was a "MemoryError" which meant I had to install it differently:
```
sudo python -m pip --no-cache-dir install matplotlib
```

### Files
* *Sensors.py* - detects movement ahead of the GrovePi+ Ultrasonic Ranger.
* This calls code from data.py and utilities.py. 
* *Data.py* contains sample code showing how its methods can be used to create graphs.
* *Camera.py* can be used to test that the camera works - it will take a photo and can be exited through a key press.
* *Real_time_object_detection.py* contains the code for, well, detecting objects.
* *main.py* combines a majority of the code developed.

### Using the project
* Each time you open a new terminal window, you need to access the virtual environment holding Python3 and OpenCV:
```
source ~/.profile
workon py3cv3
```
* To edit a file, you can use Nano or an actual IDE such as Thonny - the way to enter both are described below:
```
sudo nano ______.py
sudo thonny ______.py
```
* Note that you might need to add the relevant write permission:
```
sudo chmod a+w ______.py
```
* To execute the main file's code, sudo is required as keyboard required root privileges (this would work for other files too):
```
sudo python sensors.py
```
* Ctrl + C will trigger a 'KeyboardInterrupt' to stop the program once it is in operation.
* Real_time_object_detection.py can be called the following command (exit using a "q" key press):
```
python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel
```

### Pie chart
* Thanks for visiting the repository - I've added a screenshot of the pie chart I created, below.  
* This shows how the data collected on the meeting rooms can be used by the Department of Computer Science.  
* One idea I had involves tracking usage of the rooms across Monday-Friday - in the example below, you can see that Thursday's occupancy is much higher than the other days. In particular, Wednesday and Friday.  
* Using this, we know that students should be advised to use the rooms on such days, hopefully therefore reducing congestion.  
![Pie chart](https://i.imgur.com/Kb0AhGK.png)
