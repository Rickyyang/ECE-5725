import os
import time
import RPi.GPIO as GPIO

start_time = time.time()

GPIO.setmode(GPIO.BCM) 
#	setup
#
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

prev_22 = False

while (time.time() - start_time) < 10:
	time.sleep(0.00002)
	if not GPIO.input(17):
		# Button is pressed
		print "Button 17 has been pressed!"
		os.system("echo 'quit' > mplayer")
	if (not GPIO.input(22)) and prev_22:
		# Button is pressed
		print "Button 22 has been pressed!"
		os.system("echo 'pause' > mplayer")
	if not GPIO.input(23):
		# Button is pressed
		print "Button 23 has been pressed!"
		os.system("echo 'seek 10' > mplayer")
	if not GPIO.input(27):
		# Button is pressed
		print "Button 27 has been pressed!"
		os.system("echo 'seek -10' > mplayer")	
	prev_22 = GPIO.input(22)
