import pygame # Import Library and initialize pygame
from pygame.locals import *
import math
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
speed1 = [2,3]
speed2 = [3,5]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

##----------- set touch buttons -----------------------##
WHITE = (255,255,255)
font = pygame.font.Font(None, 30)
disp_message = 'No touch detected'
touch_buttons = {'Quit':(256,200),disp_message:(160,120)}
screen.fill(black)
##---------- function to move the ball-----------------##
			
for k,v in touch_buttons.items():
	text_surface = font.render('%s'%k, True, WHITE)
	rect = text_surface.get_rect(center=v)
	screen.blit(text_surface,rect)

pygame.display.update()

pos_down = (0,0)
hit_counter = 0

while 1:
	for event in pygame.event.get():
		if event.type is MOUSEBUTTONUP:
			pos_up = pygame.mouse.get_pos()
			disp_message = 'Mouse Released at:' + str(pos_up)
			touch_buttons = {'Quit':(256,200),disp_message:(160,120)}
			if hit_counter < 21:
				print disp_message
			elif hit_counter == 21:
				print '20 hits collected'
			if 175 < pos_down[1] < 225 and 230 < pos_down[0] < 270 and 175 < pos_up[1] < 225 and 230 < pos_up[0] < 270:  
				quit()	
		elif event.type is MOUSEBUTTONDOWN :
			pos_down = pygame.mouse.get_pos()
			disp_message = 'Hit Detected on:' + str(pos_down)
			touch_buttons = {'Quit':(256,200),disp_message:(160,120)}
			hit_counter = hit_counter + 1;
			# print disp_message
		elif event.type is MOUSEMOTION:	
			pos_moving = pygame.mouse.get_pos()
			disp_message = 'Hit Detected on:' + str(pos_moving)
			touch_buttons = {'Quit':(256,200),disp_message:(160,120)}
			# print disp_message
	#--------------  update the screen								
	screen.fill(black) # Erase the Work space
	
	for k,v in touch_buttons.items(): # Update the control buttons 
		text_surface = font.render('%s'%k, True, WHITE)
		rect = text_surface.get_rect(center=v)
		screen.blit(text_surface,rect)

	pygame.display.update() # display workspace on screen
	




