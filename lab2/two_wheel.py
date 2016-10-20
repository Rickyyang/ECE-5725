import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
left_wheel_num = 5
right_wheel_num = 6
GPIO.setup(pin_num, GPIO.OUT)

pulse_length = 1.5
Freq = 1000/(20+pulse_length)
dc = pulse_length/(20+pulse_length)*100 # duty cycle

p = GPIO.PWM(pin_num, Freq)
p.start(dc)
raw_input('press enter to continue')
start_time = time.time()
f_counter = 0
try:
	while 1:
		if time.time()-start_time >= 3:
			start_time = time.time()
			if f_counter < 10:
				pulse_length = 1.5 - 0.02 * (f_counter + 1)
				Freq = 1000/(20+pulse_length)
				dc = pulse_length/(20+pulse_length)*100
				print 'pulse_length: ',pulse_length
				print 'Frequency: ', Freq
				print 'Duty cycle: ',dc
				p.ChangeFrequency(Freq)
				p.ChangeDutyCycle(dc)
				f_counter = f_counter + 1
			elif 10 <= f_counter < 20:
				pulse_length = 1.5 + 0.02 * (f_counter-9)
				Freq = 1000/(20+pulse_length)
				dc = pulse_length/(20+pulse_length)*100
				print 'pulse_length: ',pulse_length
				print 'Frequency: ', Freq
				print 'Duty cycle: ',dc
				p.ChangeFrequency(Freq)
				p.ChangeDutyCycle(dc)
				f_counter = f_counter + 1
			elif f_counter >= 20:
				quit()
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

