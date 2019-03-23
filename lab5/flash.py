import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

flash_frequency = 2
flash_rounds = 10

for i in xrange(flash_rounds):
    print "Round: ", i
    GPIO.output(18, GPIO.HIGH)
    print "LED on"
    time.sleep(flash_frequency)
    GPIO.output(18, GPIO.LOW)
    print "LED off"
    time.sleep(flash_frequency)
    print ""
