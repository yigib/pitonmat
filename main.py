#!/usr/bin/env python
#
#  Copyright 2022 Yiğit Altınay <yigit@altinay.xyz>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.  

# colors
# white: #b58863 (181, 136, 99)
# black: #f0d9d5 (240, 217, 213)
# white played: #ced26b
# black played: #aba23a

import pygame

pygame.init()
pygame.display.set_caption('Pitonmat')

HEIGHT = 640
WIDTH  = 640
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# takes height, width. returns a dict with width for screen parts
def calculate_props(width, height):
	
	# 1 part left gui, 4 part board, 1 part right gui
	part = width / 5
	left = part
	middle = part * 4
	right = part
	
	# chess board is 8x8, this assumes middle_width == HEIGHT
	square = middle / 8
	if not square == HEIGHT / 8:
		pass
		#print('width and height of squares arent equal lol')
		
	
	return { 'left_width': left, 'middle_width': middle, 'right_width': right, 'square_width': square }
	

running = True


#SCREEN_PROPS = calculate_props(WIDTH,HEIGHT)

SIZE=HEIGHT/8

black=(181, 136, 99)
white=(240, 217, 182)

while running:
	# program should shut down when quit is pressed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
            
            
	screen.fill( (255,255,255) )
	
	for row in range(0,8):
		for column in range(0,8):
			rect= pygame.Rect(row*SIZE, column*SIZE, SIZE, SIZE)
			sqr_color = white if (row+column+1)%2 else black
			pygame.draw.rect(screen, sqr_color, rect)
			
	
	
	pygame.display.flip()

pygame.quit()
