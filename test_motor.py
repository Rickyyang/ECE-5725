import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(5, GPIO.OUT)

pulse_length = 1.5
Freq = 1000/(20+pulse_length)
dc = pulse_length/(20+pulse_length)*100 # duty cycle

p = GPIO.PWM(5, Freq)
p.start(dc)
raw_input('press enter to continue')
start_time = time.time()
f_counter = 1
while 1:
	if time.time()-start_time >= 3
		start_time = time.time()
		
	time = time.time()
	a = float(input('Press return to stop:'))   # use raw_input for Python 2
	pulse_length = pulse_length + a/10
	Freq = 1000/(20+pulse_length)
	dc = pulse_length/(20+pulse_length)*100
	print 'pulse_length: ',pulse_length
	print 'Duty cycle: ',dc
	p.ChangeFrequency(Freq)
	p.ChangeDutyCycle(dc)
	
p.stop()
GPIO.cleanup()
