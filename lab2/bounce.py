import pygame # Import Library and initialize pygame

pygame.init()

size = width, height = 320, 240
speed = [2,2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("../python_games/4row_red.png")
ballrect = ball.get_rect()
while 1:
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	screen.fill(black) # Erase the Work space
	screen.blit(ball, ballrect) # Combine Ball surface with workspace surface
	pygame.display.flip() # display workspace on screen
