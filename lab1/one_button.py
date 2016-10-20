import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	time.sleep(0.2)
	if not GPIO.input(27):
		print "Button 27 has beebash n pressed!"
