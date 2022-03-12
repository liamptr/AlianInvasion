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

#set fps
fps=60

#give background
bg = pygame.transform.scale(pygame.image.load(
    'C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\space.png'), (width , height))

def draw():
     win.blit(bg,(0,0))
     
     
     

    
def main():
    clock=pygame.time.Clock()
    run=True
    
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run=False
        draw()
         
        pygame.display.update()       
    pygame.quit()     
                 

if __name__ == '__main__':        
     main()        
    
    