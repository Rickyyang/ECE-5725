import pygame # Import Library and initialize pygame
from pygame.locals import *
import math
import os
import time
import RPi.GPIO as GPIO
import subprocess

##----------- start the bounce ball -------------------##

subprocess.call('sudo python test.py',shell=True)

aaa = 1
#~ ##----------- set system param to output to TFT---------##
#~ os.putenv('SDL_VIDEODRIVER','fbcon')
#~ os.putenv('SDL_FBDEV', '/dev/fb1')
#~ os.putenv('SDL_MOUSEDRV', 'TSLIB')
#~ os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
#~ 
#~ ##----------- init screen--- --------------------------##
#~ pygame.init()
#~ 
#~ pygame.mouse.set_visible(False)
#~ size = width, height = 320, 240
#~ 
#~ ##----------- set touch buttons -----------------------##
#~ WHITE = (255,255,255)
#~ font = pygame.font.Font(None, 30)
#~ touch_buttons = {'Start':(64,200), 'Quit':(256,200)}
#~ 
#~ screen.fill(black)
#~ ##---------- function to move the ball-----------------##
#~ 
			#~ 
#~ for k,v in touch_buttons.items():
	#~ text_surface = font.render('%s'%k, True, WHITE)
	#~ rect = text_surface.get_rect(center=v)
	#~ screen.blit(text_surface,rect)
#~ 
#~ pygame.display.update()
#~ 
#~ hit_counter = 0		# init hit counter
#~ 
#~ start_the_bounce = False # do not start the animation at first
#~ sleep_time = 0.05	#param to control the speed
#~ 
#~ #-------------- send param ----------------------------##
#~ 
#~ while 1:
	#~ time.sleep(sleep_time)
		#~ 
	#~ for event in pygame.event.get():
		#~ if event.type is MOUSEBUTTONDOWN:
			#~ pos = pygame.mouse.get_pos()
			#~ print pos
		#~ elif event.type is MOUSEBUTTONUP:
			#~ pos = pygame.mouse.get_pos()
			#~ print pos
			#~ if 175 < pos[1] < 225 :  #and pos[2] > 175 :
				#~ if 40 < pos[0] < 80 :	# if start/pause button is pressed
					#~ if start_the_bounce:
						#~ touch_buttons['Start'] = touch_buttons.pop('Pause')
					#~ elif not start_the_bounce: 
						#~ touch_buttons['Pause'] = touch_buttons.pop('Start')
					#~ start_the_bounce = not start_the_bounce
				#~ elif 230 < pos[0] < 270:
					#~ quit()
		#~ 
	#~ #-------------- update the ball movement
	#~ 
	#~ #--------------  update the screen								
	#~ screen.fill(black) # Erase the Work space
	#~ for k,v in touch_buttons.items(): # Update the control buttons 
		#~ text_surface = font.render('%s'%k, True, WHITE)
		#~ rect = text_surface.get_rect(center=v)
		#~ screen.blit(text_surface,rect)
#~ 
	#~ pygame.display.update() # display workspace on screen
	




