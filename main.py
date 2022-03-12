# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:25:34 2022

@author: ssssa
"""

import pygame

#set display
width , height = 900 , 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('space')

spaceship_width, spaceship_height = 55, 40
#set fps
fps=60

#give background
bg = pygame.transform.scale(pygame.image.load(
    'C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\space.png'), (width , height))
#give spaceships

red_space_ship=pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load('C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\spaceship_red.png'), 
        (spaceship_width, spaceship_height)), 90)
yellow_space_ship=pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load('C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\spaceship_yellow.png'), 
        (spaceship_width, spaceship_height)), 270)



def draw(red,yellow):
     win.blit(bg,(0,0))
     win.blit(red_space_ship,(red.x,red.y))
     win.blit(yellow_space_ship,(yellow.x,yellow.y))
#set movment     
def red_movment(keys,red):
    if keys[pygame.K_a] and red.x - 5 > 0:
        red.x -= 5
    if keys[pygame.K_d] and red.x + 5 < width // 2:
        red.x += 5
    if keys[pygame.K_w] and red.y -5 > 0 :
        red.y -= 5
    if keys[pygame.K_s]  and red.y + 5 < height - spaceship_height :
        red.y += 5
        
def yellow_movment(keys,yellow):
    if keys[pygame.K_LEFT] and yellow.x - 5 > width // 2:
        yellow.x -= 5
    if keys[pygame.K_RIGHT] and yellow.x + 5 < width - spaceship_width :
        yellow.x += 5
    if keys[pygame.K_UP] and yellow.y -5 > 0 :
        yellow.y -= 5
    if keys[pygame.K_DOWN]  and yellow.y + 5 < height - spaceship_height :
        yellow.y += 5
    
     

    
def main():
    clock=pygame.time.Clock()
    run=True
    red=pygame.Rect(width//8, height//2, 300, 400)
    yellow=pygame.Rect(width - (width//8),height//2, width, height)
    
    while run:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run=False
        draw(red,yellow)
        keys=pygame.key.get_pressed()
        red_movment(keys, red)
        yellow_movment(keys,yellow)
        
        pygame.display.update()       
    pygame.quit()     
                 

if __name__ == '__main__':        
     main()        
    
    