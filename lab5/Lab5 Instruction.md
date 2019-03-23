# Lab5 Instruction

-- by Fangyu Gai. Any questions --> fangyu.gai@ubc.ca

---

In lab5, we will connect our Pi to a LED and make it flashing! 
Don't worry, this lab is going to be much easier than last one.

## Task 1 Connect your Raspberry Pi to a LED

Please follow this [link](https://www.youtube.com/watch?v=BWYy3qZ315U) to finish task 1.
You may need a monitor to get the IP address of the Pi and connect it with your computer using ssh, and then test the LED via Python interactive console (in the end of the video).

Note that our model is different with the one used in the video, so the GPIO pins is a little bit different.
You can find the difference in the following figure. 

![](https://cdn.shopify.com/s/files/1/0176/3274/files/Pins_Only_grande.png?2408547127755526599)

## Task 2 Make LED flash

Affter the installation, we will write some code to the Pi to make the LED flash.

You can download the code `flash.py` written in Python from Canvas and open it using whatever editors you like.
To have a better understanding of the code, please go through the flowing explanations.

1. `import RPi.GPIO as GPIO`: The first line tells the Python interpreter (the thing that runs the Python code) that it will be using a ‘library’ that will tell it how to work with the Raspberry Pi’s GPIO pins.  A ‘library’ gives a programming language extra commands that can be used to do something different that it previously did not know how to do.  This is like adding a new channel to your TV so you can watch something different.
2. `import time`: Imports the Time library so that we can pause the script later on.
3. `GPIO.setmode(GPIO.BCM)` Each pin on the Raspberry Pi has several different names, so you need to tell the program which naming convention is to be used.
4. `GPIO.setwarnings(False)`: This tells Python not to print GPIO warning messages to the screen.
5. `GPIO.setup(18,GPIO.OUT)`: This line tells the Python interpreter that pin 18 is going to be used for outputting information, which means you are going to be able to turn the pin ‘on’ and ‘off’.
5. `flash_frequency = 2` This variable determines the flash frequency of the LED to be 2 seconds between each on and off. You can change this number to an alternative value you like.
6. `flash_rounds = 10` This variable determines the total rounds of flashing. You can change this number to an alternative value you like.
7. `for i in xrange(10):` 