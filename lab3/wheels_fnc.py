import RPi.GPIO as GPIO

class Wheel:
	def __init__(self, side, Pin_num):
		self.pin_num = Pin_num
		self.side_name = side
		if side == 'left':
			self.side = 1
		elif side == 'right':
			self.side = -1
		else:
			print('invalid initialization!')
		GPIO.setup(Pin_num, GPIO.OUT)
		self.pulse_length = 1.5
		self.Freq = 1000/(20+self.pulse_length)
		self.dc = self.pulse_length/(20+self.pulse_length)*100 	# duty cycle
		self.p = GPIO.PWM(Pin_num, self.Freq)
		self.p.start(self.dc)
		self.speed = 0		#initial speed
		
	def PWM_change(self):
		self.Freq = 1000/(20 + self.pulse_length)
		self.dc = self.pulse_length/(20 + self.pulse_length)*100 	# duty cycle
		self.p.ChangeFrequency(self.Freq)
		self.p.ChangeDutyCycle(self.dc)
				
	def movement(self, move = 'stop', spd = 'stable'):
		self.move = move
		if type(spd) == str:
			if spd == 'faster':
				self.speed = self.speed + 1
			elif spd == 'slower':
				self.speed = self.speed - 1
			elif spd == 'stable':
				self.speed = self.speed
			elif spd == 'median':
				self.speed = 5
			else: 
				print('wrong speed input')
		elif type(spd) == int:
			self.speed = spd

		if self.speed > 10: #limit speed from 1 to 10
			self.speed = 10
		elif self.speed < 1:
			self.speed = 1
			
		if move == 'stop':
			self.pulse_length = 1.5
			self.PWM_change()
		elif move == 'forward':
			self.pulse_length = 1.5 + self.side * self.speed * 0.02
			self.PWM_change()
		elif move == 'backward':
			self.pulse_length = 1.5 - self.side * self.speed * 0.02
			self.PWM_change()
		