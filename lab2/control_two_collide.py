## control buttons added for the ball collision
## author : Ziqi Yang, zy259, Haowen Tao, ht398

import pygame # Import Library and initialize pygame
from pygame.locals import *
import math
import os
import time
import RPi.GPIO as GPIO

##----------- set GPIO for force exit-------##
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GPIO17_callback(channel):
	pygame.quit()
	
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback,bouncetime=300)

##----------- set system param to output to TFT---------##
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

##----------- init ball param --------------------------##
pygame.init()

pygame.mouse.set_visible(False)
size = width, height = 320, 240
speed1 = [2,3]
speed2 = [3,5]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball1 = pygame.image.load("../python_games/4row_red.png")
ball1 = pygame.transform.scale(ball1,(30,30))
ball1rect = ball1.get_rect()

ball2 = pygame.image.load("../python_games/4row_red.png")
ball2 = pygame.transform.scale(ball2,(30,30))
ball2rect = ball2.get_rect()

##----------- set touch buttons -----------------------##
WHITE = (255,255,255)
font = pygame.font.Font(None, 30)
touch_buttons = {'Start':(64,200), 'Back':(256,200)}

screen.fill(black)
##---------- function to move the ball-----------------##

			
for k,v in touch_buttons.items():
	text_surface = font.render('%s'%k, True, WHITE)
	rect = text_surface.get_rect(center=v)
	screen.blit(text_surface,rect)

pygame.display.update()

##---------- param initialization ---------------------##
hit_counter = 0		# init hit counter
start_the_bounce = False # do not start the animation at first
sleep_time = 0.05	#param to control the speed
pos_down = (0,0)
move_the_ball = 0

while 1:
	for event in pygame.event.get():
		if event.type is MOUSEBUTTONDOWN:
			pos_down = pygame.mouse.get_pos()
			move_the_ball = 0
			dist_finger_ball1_x = pos_down[0] - ball1rect.center[0]
			dist_finger_ball1_y = pos_down[1] - ball1rect.center[1]
			dist_finger_ball1 = math.hypot(dist_finger_ball1_x, 
											dist_finger_ball1_y)
			dist_finger_ball2_x	= pos_down[0] - ball2rect.center[0] 	
			dist_finger_ball2_y = pos_down[1] - ball2rect.center[1]
			dist_finger_ball2 = math.hypot(dist_finger_ball2_x, 
											dist_finger_ball2_y)								
			if  dist_finger_ball1 <= 30: 
				move_the_ball = 1
			elif dist_finger_ball2 <= 30:
				move_the_ball = 2
		elif event.type is MOUSEMOTION:
			pos_moving = pygame.mouse.get_pos()
			if move_the_ball == 1 : # if not start allow change the ball pos
				dist_finger_ball1_x = pos_moving[0] - ball1rect.center[0]
				dist_finger_ball1_y = pos_moving[1] - ball1rect.center[1]
				ball1rect = ball1rect.move([dist_finger_ball1_x,dist_finger_ball1_y])
			elif move_the_ball == 2 :
				dist_finger_ball2_x = pos_moving[0] - ball2rect.center[0]
				dist_finger_ball2_y = pos_moving[1] - ball2rect.center[1]
				ball2rect = ball2rect.move([dist_finger_ball2_x,dist_finger_ball2_y])
		elif event.type is MOUSEBUTTONUP:
			move_the_ball = 0
			pos = pygame.mouse.get_pos()
			print pos
			if 175 < pos[1] < 225 :  #and pos[2] > 175 :
				if 40 < pos[0] < 80 :	# if start/pause button is pressed
					if start_the_bounce:
						touch_buttons['Start'] = touch_buttons.pop('Pause')
						touch_buttons['Fast'] = (128,200) #'Fast':(128,200), 'Slow':(192,200),
						touch_buttons['Slow'] = (192,200)
						touch_buttons.pop('Fast',None)
						touch_buttons.pop('Slow',None)						
					elif not start_the_bounce: 
						touch_buttons['Pause'] = touch_buttons.pop('Start')
						touch_buttons['Fast'] = (128,200) #'Fast':(128,200), 'Slow':(192,200),
						touch_buttons['Slow'] = (192,200)
						touch_buttons_add = 0
					start_the_bounce = not start_the_bounce
				elif 105 < pos[0] < 140: # if Fast button
					sleep_time = sleep_time / 2
				elif 170 < pos[0] < 210: # if Slow button
					sleep_time = sleep_time * 2;
				elif 230 < pos[0] < 270:
					quit()
		
	#-------------- update the ball movement
	if start_the_bounce:
		time.sleep(sleep_time)	
		ball1rect = ball1rect.move(speed1)
		ball2rect = ball2rect.move(speed2)
		if ball1rect.left < 0 or ball1rect.right > width:
			speed1[0] = -speed1[0]
		if ball1rect.top < 0 or ball1rect.bottom > height:
			speed1[1] = -speed1[1]			
		if ball2rect.left < 0 or ball2rect.right > width:
			speed2[0] = -speed2[0]
		if ball2rect.top < 0 or ball2rect.bottom > height:
			speed2[1] = -speed2[1]	
		
		# check ball distance
		dist = math.hypot(ball1rect.center[0] - ball2rect.center[0], 
							ball1rect.center[1] - ball2rect.center[1])
		# check the collicion & add hit counter to prevent ball stick to each other
		if dist <= 30 and hit_counter ==0:
			speed1,speed2 = speed2,speed1 
			hit_counter = 100;
			print "hit"
		elif hit_counter > 0:
			hit_counter -= 1
	#--------------  update the screen								
	screen.fill(black) # Erase the Work space
	screen.blit(ball1, ball1rect) # Combine Ball surface with workspace surface
	screen.blit(ball2, ball2rect) # Combine Ball surface with workspace surface
	for k,v in touch_buttons.items(): # Update the control buttons 
		text_surface = font.render('%s'%k, True, WHITE)
		rect = text_surface.get_rect(center=v)
		screen.blit(text_surface,rect)

	pygame.display.update() # display workspace on screen
	




