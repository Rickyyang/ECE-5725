import pygame # Import Library and initialize pygame
from datetime import datetime
from pygame.locals import *
from wheels_fnc import Wheel
import RPi.GPIO as GPIO
import os
import time

##----------- set system param to output to TFT---------##
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

##----------- init ball param --------------------------##
pygame.init()

pygame.mouse.set_visible(False)
size = width, height = 320, 240
black = 0, 0, 0
screen = pygame.display.set_mode(size)

##----------- set touch buttons -----------------------##
WHITE = (255,255,255)
font = pygame.font.Font(None, 20)
touch_buttons = {'left':(110,120), 'right':(220,120), 'fordward':(70,160), 'backward': (180,160), 'stop':(280,160),  'faster':(50,200), 'slower':(220,200), 'quit':(130,200)}


## ---------- display commands ------------------------##
first = ''
second = ' '
third = '  '
Command = {first: (200,30),second:(200,50),third:(200,80)} 

screen.fill(black)
for k,v in touch_buttons.items():
	text_surface = font.render('%s'%k, True, WHITE)
	rect = text_surface.get_rect(center=v)
	screen.blit(text_surface,rect)

for k,v in Command.items():
	text_surface = font.render('%s'%k, True, WHITE)
	rect = text_surface.get_rect(center=v)
	screen.blit(text_surface,rect)

pygame.display.update()


def Command_fifo(cmd):
	global first, second, third, Command
	third = second
	second = first
	first = cmd
	print('cmd:', cmd)
	Command = {first: (150,30),second:(150,50),third:(150,80)} 
	print(Command)

GPIO.setmode(GPIO.BCM)			
right_wheel = Wheel('right', 6)
left_wheel = Wheel('left', 5)
start_time = time.time()
stopped = 0

try:
	while 1:	
		for event in pygame.event.get():
			if event.type is MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if 100 < pos[1] < 140 :
					if 90 < pos[0] < 130:
						left_wheel.movement('stop')
						right_wheel.movement('stop')
						wheel_testing = left_wheel
						cmd = str(datetime.now()) + ': ' +'left wheel selected'
						Command_fifo(cmd)
					elif 200 < pos[0] < 240 :
						left_wheel.movement('stop')
						right_wheel.movement('stop')
						wheel_testing = right_wheel
						cmd = str(datetime.now()) + ': ' +'right wheel selected'
						Command_fifo(cmd)
				elif 140 < pos[1] < 180 :  #and pos[2] > 175 :
					if 70 < pos[0] < 90 :	# if first button is pressed
						wheel_testing.movement('forward','median')
						mov = 'forward'
						cmd = str(datetime.now()) + ': ' + str(wheel_testing.side_name) +' wheel forward'
						Command_fifo(cmd)
					elif 160 < pos[0] < 200: # if Fast button
						wheel_testing.movement('backward','median')
						mov = 'backward'
						cmd = str(datetime.now()) + ': ' + str(wheel_testing.side_name) +' wheel backward'
						Command_fifo(cmd)
					elif 260 < pos[0] < 300:
						print('stopped:',stopped)
						if 	stopped == 0:
							left_wheel.movement('stop')
							right_wheel.movement('stop')
							touch_buttons['Resume'] = touch_buttons.pop('stop')
							stopped = 1
							cmd = str(datetime.now()) + ': stopped' 
							Command_fifo(cmd)
						elif stopped == 1:
							touch_buttons['stop'] = touch_buttons.pop('Resume')
							stopped = 0
							cmd = str(datetime.now()) + ': continued' 
							Command_fifo(cmd)
				elif 190 < pos[1] < 220:
					if 30 < pos[0] < 80: # if Slow button
						wheel_testing.movement(mov,'faster')
						cmd = str(datetime.now()) + ': ' + str(wheel_testing.side_name) +' wheel faster'
						Command_fifo(cmd)
					elif 200 < pos[0] < 240:
						wheel_testing.movement(mov,'slower')
						cmd = str(datetime.now()) + ': ' + str(wheel_testing.side_name) +' wheel slower'
						Command_fifo(cmd)
					elif 120 < pos[0] < 155:
						GPIO.cleanup()
						quit()
						
		screen.fill(black)				
		for k,v in touch_buttons.items():
			text_surface = font.render('%s'%k, True, WHITE)
			rect = text_surface.get_rect(center=v)
			screen.blit(text_surface,rect)
		for k,v in Command.items():
			text_surface = font.render('%s'%k, True, WHITE)
			rect = text_surface.get_rect(center=v)
			screen.blit(text_surface,rect)
		pygame.display.update() # display workspace on screen
except KeyboardInterrupt:
	GPIO.cleanup()	
	
