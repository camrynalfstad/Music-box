# Music-Box
# About The Project
This project combines Python programming and a Raspberyy Pi, to create a sound system that can be accessed through interactive buttons. The Pi is equipped with four tactile buttons which when pressed will play a certain beat or sound. The goal of this project is to give users access to a variety of different beats that provide an enjoyable experience. 

The system wull function using Pygame to create an interactive music player, with buttons to control each sound. This will be done using a dictionary that assigns each button to play a downloaded sound when pressed. The speaker which is connected to the Pi will then play the assigned sound.

# List of Materials
-Raspberry Pi with multiple USB ports
-Power supply for Raspberry Pi
-Four tactile buttons
-Nine Male to Male wires
-USB Speaker
-Python Libraries: Pygame, GPIOzero, Button, and pause

# How to wire
-Place the four tactile buttons with each set of prongs on either side of the middle of the breadboard
-Connect one set of prongs on each tactile button to Ground
-Connect the other set of prongs on button 1 to pin 22
-Repeat step 3 for each tactile button connecting to pins 21,20, and 19
-Plug the USB Speaker into one of the USB ports located on the Pi

# How to Run the Program
1. Setup Raspberry Pi by installing the proper libraries
   pip install pygame
   pip install gpiozero
   pip install signal

2. Download and transfer Music Files
   Go to rpf.io/p/en/gpio-music-box-go and select your desired sounds. Then place them in the directory where the python file is located on the raspberry Pi.

3. Run Python Script
   python music.py

# What Does the Code Do?
The main component of this code is assigning the sounds to the buttons. 
This part uses a dictionary to assign each button using their pins to a sound. By using pygame.mixer.Sound it allows you to acces your downloaded files and input them into the program. 
For more information, refrence the Python script music.py, which contains the code written line by line. 

# Resources
- gpiozero:https://gpiozero.readthedocs.io/en/stable/recipes.html
- Raspberry Pi Foundation: https://projects.raspberrypi.org/en/projects/gpio-music-box
- Music Download: rpf.io/p/en/gpio-music-box-go

