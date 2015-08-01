import random
import pygame
from pygame.locals import *
import time
import threading

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NAVY = (0, 0, 128)
DEEP_SKY_BLUE = (0, 191, 255)
DARK_TURQUOISE = (0, 206, 209)
STEEL_BLUE = (70, 130, 180)
BLUE = (0, 0, 255)
MEDIUM_BLUE = (0, 0, 205)
CORNFLOWER_BLUE = (100, 149, 237)
DODGER_BLUE = (30, 144, 255)
colors = [BLACK, NAVY, DEEP_SKY_BLUE, DARK_TURQUOISE, 
         STEEL_BLUE, BLUE, MEDIUM_BLUE, CORNFLOWER_BLUE, DODGER_BLUE]

SCREEN_SIZE = screen_width, screen_height = 1000, 700
width = random.randrange(5, 10, 1)

class Circle:
	def __init__(self, x, y, radius, color, width):
		self.x = x
		self.y = y
		self.radius = radius
		self.width = width
		self.color = color

	def draw(self, screen_to_draw_on):
		pygame.draw.circle(
			screen_to_draw_on, 
			self.color,
			(self.x, self.y),
			self.radius,
			self.width 
		)

screen = pygame.display.set_mode(SCREEN_SIZE) 

xy_cor = [[150,400],[150,600],[350,400],[350,600],
          [200,450],[200,550],[300,450],[300,550],
          [175,425],[175,575],[225,475],[225,525],
          [275,475],[275,525],[325,425],[325,575],
          [250,500],
          [650,400],[650,420],[650,450],[650,480],
          [650,500],[650,520],[650,550],[650,580],
          [650,600],
          [900,400],[750,600],[750,400],[750,480],
          [750,400],[780,400],[825,400],[850,400],[880,400],
          [800,400],[750,425],[750,450],
          [750,480],[780,480],[825,480],[850,480],[880,480],
          [800,480],[900,480],
          [750,600],[780,600],[825,600],[850,600],[880,600],
          [800,600],[900,600],
          [900,500],[900,520],[900,550],[900,580],
          [900,600],
          [500,400],[500,420],[500,450],[500,480],
         [300,300],[275,300],[250,300],[225,300],[250,300],[225,300],[200,300],[175,300],[150,300],[100,100],[300,100],[100,300],[125,300],
         [300,100],[275,100],[250,100],[225,100],[250,100],[225,100],[200,100],[175,100],[150,100],[125,100],
         [100,125],[100,150],[100,175],[100,200],[100,225],[100,250],[100,275],
         [400,300],[425,300],[450,300],[475,300],[500,300],[525,300],[550,300],[575,300],[600,300],
         [500,100],[500,125],[500,150],[500,175],[500,200],[500,225],[500,250],[500,275],
         [400,200],[425,200],[450,200],[475,200],[500,200],[525,200],[550,200],[575,200],[600,200],
         [400,200],[400,225],[400,250],[400,275],
         [500,250],[525,250],[550,250],[575,250],[600,250],[600,225],

         [900,300],[875,300],[850,300],[825,300],[850,300],[825,300],[800,300],[775,300],[750,300],[700,100],[900,100],[700,300],[725,300],
         [900,100],[875,100],[850,100],[825,100],[850,100],[825,100],[800,100],[775,100],[750,100],[725,100],
         [700,125],[700,150],[700,175],[700,200],[700,225],[700,250],[700,275],

  #         [180,50],[110,100],[250,60],[100,155],[100,230],
		# [160,300],[240,310],[510,80],[510,150],[510,230],[510,310],
		# [510,680],[450,200],[340,235],[340,310],[410,320],
		# [830,50],[760,100],[900,55],[750,155],[750,230],
		# [810,300],[890,310],[520,200],[560,250],[570,300],[620,330],[660,300]
       ]
number_of_circles = len(xy_cor)
print number_of_circles
circles = []

def wait():
	return time.clock()

for cor in range(number_of_circles):
	radius = random.randint(10, 15)
	x = xy_cor[cor][0]
	y = xy_cor[cor][1]
	color = random.choice(colors)
	circles.append(Circle(x, y, radius, color, width))

running = True 

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False 

	#Make the background white
	screen.fill(WHITE)
	#Draw the cirlce on the screen canvas
	#pygame.draw.line()
	# pygame.draw.line(screen, BLUE, [100, 0], [100,1000], 1)
	# pygame.draw.line(screen, BLUE, [200, 0], [200,1000], 1)
	# pygame.draw.line(screen, BLUE, [300, 0], [300,1000], 1)
	# pygame.draw.line(screen, BLUE, [400, 0], [400,1000], 1)
	# pygame.draw.line(screen, BLUE, [500, 0], [500,1000], 1)
	# pygame.draw.line(screen, BLUE, [600, 0], [600,1000], 1)
	# pygame.draw.line(screen, BLUE, [700, 0], [700,1000], 1)
	# pygame.draw.line(screen, BLUE, [800, 0], [800,1000], 1)
	# pygame.draw.line(screen, BLUE, [900, 0], [900,1000], 1)
	# pygame.draw.line(screen, BLUE, [1000, 0], [1000,1000], 1)

	# pygame.draw.line(screen, BLUE, [0, 100], [1000,100], 1)
	# pygame.draw.line(screen, BLUE, [0, 200], [1000,200], 1)
	# pygame.draw.line(screen, BLUE, [0, 300], [1000,300], 1)
	# pygame.draw.line(screen, BLUE, [0, 400], [1000,400], 1)
	# pygame.draw.line(screen, BLUE, [0, 500], [1000,500], 1)
	# pygame.draw.line(screen, BLUE, [0, 600], [1000,600], 1)
	# pygame.draw.line(screen, BLUE, [0, 700], [1000,700], 1)


	if wait() <= 5:
		for circle in circles:
			n = time.clock()
			if wait() <= n:
				circle.draw(screen)
	else:
		for circle in circles:
			circle.draw(screen)

	pygame.display.flip() 

pygame.quit()