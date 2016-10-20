import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 
#	setup
#
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	time.sleep(0.2)
	if not GPIO.input(17):
		# Button is pressed
		print "Button 17 has been pressed!"
	if not GPIO.input(22):
		# Button is pressed
		print "Button 22 has been pressed!"
	if not GPIO.input(23):
		# Button is pressed
		print "Button 23 has been pressed!"
	if not GPIO.input(27):
		# Button is pressed
		print "Button 27 has been pressed!"	
