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
GPIO.setup(5 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6 , GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GPIO22_callback(channel):
	os.system("echo 'pause' > mplayer")

def GPIO23_callback(channel):
	os.system("echo 'seek 10' > mplayer")

def GPIO27_callback(channel):
	os.system("echo 'seek -10' > mplayer")

def GPIO5_callback(channel):
	os.system("echo 'seek 30' > mplayer")

def GPIO6_callback(channel):
	os.system("echo 'seek -30' > mplayer")

# GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback,bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback,bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback,bouncetime=300)
GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback,bouncetime=300)
# GPIO.add_event_detect(5, GPIO.FALLING, callback=GPIO5_callback,bouncetime=300)
GPIO.add_event_detect(6, GPIO.FALLING, callback=GPIO6_callback,bouncetime=300)

try:
	# time.sleep(0.01) # doesn't fix it
	GPIO.wait_for_edge(5, GPIO.FALLING)
	os.system("echo 'quit' > mplayer")
	print "Quit!"
except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
