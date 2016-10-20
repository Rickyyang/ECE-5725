import pygame # Import Library and initialize pygame
import math
import time
import os
import RPi.GPIO as GPIO

##----------- set GPIO for force exit-------##
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GPIO17_callback(channel):
	quit()
	
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback,bouncetime=300)

#~ os.putenv('SDL_VIDEODRIVER','fbcon')
#~ os.putenv('SDL_FBDEV', '/dev/fb0')
#~ os.putenv('SDL_MOUSEDRV', 'TSLIB')
#~ os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()

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

hit_counter = 0

while 1:
	time.sleep(0.01)
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

	screen.fill(black) # Erase the Work space
	screen.blit(ball1, ball1rect) # Combine Ball surface with workspace surface
	screen.blit(ball2, ball2rect) # Combine Ball surface with workspace surface
	pygame.display.flip() # display workspace on screen
