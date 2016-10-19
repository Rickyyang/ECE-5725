import RPi.GPIO as GPIO
import time
from wheels_fnc import Wheel
GPIO.setmode(GPIO.BCM)

pin_left = 5 # gpio 5 for left
pin_right = 6 # gpio 6 for right
			
right_wheel = Wheel('right', 6)
left_wheel = Wheel('left', 5)
start_time = time.time()

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while 1:

		time.sleep(0.2)
		if not GPIO.input(17):
			left_wheel.movement('forward','median')
		if not GPIO.input(22):
			left_wheel.movement('backward','median')
		if not GPIO.input(23):
			right_wheel.movement('forward','median')
		if not GPIO.input(27):
			right_wheel.movement('backward','median')
		
except KeyboardInterrupt:
	GPIO.cleanup()	
	
