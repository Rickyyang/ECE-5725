import pygame # Import Library and initialize pygame
from datetime import datetime
from pygame.locals import *
import RPi.GPIO as GPIO
import time
import os
from wheels_fnc import Wheel

GPIO.setmode(GPIO.BCM)

right_wheel = Wheel('right', 6)
left_wheel = Wheel('left', 5)

def robot_move(fnc,speed = 'median'):
	global right_wheel, left_wheel
	if fnc == 'stop':
		right_wheel.movement('stop')
		left_wheel.movement('stop')
	elif fnc == 'forward':
		right_wheel.movement('forward','median')
		left_wheel.movement('forward','median')
	elif fnc == 'backward':
		right_wheel.movement('backward','median')
		left_wheel.movement('backward','median')
	elif fnc == 'pivot left':
		left_wheel.movement('backward','median')
		right_wheel.movement('forward','median')
	elif fnc == 'pivot right':
		left_wheel.movement('forward','median')
		right_wheel.movement('backward','median')

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
touch_buttons = {'fordward':(70,160), 'backward': (180,160), 'stop':(280,160),  'pivot left':(50,200), 'pivot right':(130,200), 'quit':(220,200)}


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
	Command = {first: (150,30),second:(150,50),third:(150,70)} 
	
stopped = 0
mov = 'stop'
movement = ['forward','backward','pivot left','pivot right']
i = 0
start_time = time.time()

try:
	while 1:
		for event in pygame.event.get():
			if event.type is MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if 140 < pos[1] < 180 :  #and pos[2] > 175 :
					if 70 < pos[0] < 90 :	# if first button is pressed
						mov = 'forward'
						robot_move(mov)
						cmd = str(datetime.now()) + ': robot forward'
						Command_fifo(cmd)
					elif 160 < pos[0] < 200: # if Fast button
						mov = 'backward'
						robot_move(mov)
						cmd = str(datetime.now()) + ': robot backward'
						Command_fifo(cmd)
					elif 260 < pos[0] < 300:
						if 	stopped == 0:
							mov_stp = 'stop'
							robot_move(mov_stp)
							touch_buttons['Resume'] = touch_buttons.pop('stop')
							stopped = 1
							cmd = str(datetime.now()) + ': stopped' 
							Command_fifo(cmd)
						elif stopped == 1:
							print(mov)
							robot_move(mov)
							touch_buttons['stop'] = touch_buttons.pop('Resume')
							stopped = 0
							cmd = str(datetime.now()) + ': continued' 
							Command_fifo(cmd)
				elif 190 < pos[1] < 220:
					if 30 < pos[0] < 80: # if Slow button
						mov = 'pivot left' 
						robot_move(mov)
						cmd = str(datetime.now()) + ': pivot left'
						Command_fifo(cmd)
					elif 200 < pos[0] < 240:
						GPIO.cleanup()
						quit()
					elif 120 < pos[0] < 155:
						mov = 'pivot right'
						robot_move(mov)
						cmd = str(datetime.now()) + ': pivot right'
						Command_fifo(cmd)
##---------------------------
		robot_move(movement[i])
		cmd = str(datetime.now()) + ': robot ' + movement[i]
		Command_fifo(cmd)
		print(time.time() - start_time)
		if time.time() - start_time >= 2:
			robot_move('stop')
			i = i + 1
			if i >= 4:
				i = 0
			start_time = time.time()


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
	
except KeyboardInterrupt:
	GPIO.cleanup()	
	
