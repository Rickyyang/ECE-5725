import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

p = GPIO.PWM(5, 1)
p.start(50)
raw_input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()
