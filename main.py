# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:09:31 2022

@author: ssssa
"""
import pygame
pygame.font.init()
pygame.mixer.init()
#make window
width , height = 900 , 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('SPACE')

#set sound
bullet_hit_sound = pygame.mixer.Sound('C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\Assets_Grenade+1.mp3')
bullet_fire_sound = pygame.mixer.Sound('C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\Assets_Gun+Silencer.mp3')


#set font
health_font = pygame.font.SysFont('comicsans', 40)
winner_font = pygame.font.SysFont('comicsans', 100)

#make FPS
fps=60
#set bullets
max_bullets=3
#make hit event
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

#give background
bg = pygame.transform.scale(pygame.image.load(
    'C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\space.png'), (width, height))

#give spacdships
space_ship_width , space_ship_height = 55 , 40
yellow_space_ship = pygame.image.load(
    'C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\spaceship_yellow.png')
yellow_space_ship=pygame.transform.scale(yellow_space_ship, (space_ship_width,space_ship_height))
yellow_space_ship=pygame.transform.rotate(yellow_space_ship, 90)

red_space_ship = pygame.image.load(
    'C:\\Users\\ssssa\\Desktop\\AI remote\\assets\\spaceship_red.png')
red_space_ship=pygame.transform.scale(red_space_ship, (space_ship_width,space_ship_height))
red_space_ship=pygame.transform.rotate(red_space_ship, 270)

#define update dcreen
def draw(yellow,red,red_bullet,yellow_bullet,red_health,yellow_helath): 
    
    win.blit(bg,(0,0))
    rh_text = health_font.render('HEALTH:{}'.format(red_health),1,(255,0,0))
    yh_text = health_font.render('HEALTH:{}'.format(yellow_helath), 1, (255,255,0))
    win.blit(yh_text,(0,0))
    win.blit(rh_text,(width-(rh_text.get_width()),0))
    win.blit(yellow_space_ship,(yellow.x,yellow.y))
    win.blit(red_space_ship,(red.x,red.y))
    
    for bull in red_bullet:
        pygame.draw.rect(win,(255,0,0),bull)
    for bul in yellow_bullet:
        pygame.draw.rect(win,(255,255,0),bul)
        

    pygame.display.update()  

def yellow_movment(keys,yellow):
    if keys[pygame.K_a] and yellow.x - 5 > 0:
        yellow.x -= 5
    if keys[pygame.K_d] and yellow.x + 5 < width//2 :
        yellow.x += 5
    if keys[pygame.K_w] and yellow.y - 5 > 0 :
        yellow.y -= 5
    if keys[pygame.K_s] and yellow.y + 5 < height - space_ship_height :
        yellow.y += 5

def red_movment(keys,red):
    if keys[pygame.K_RIGHT] and red.x + 5 < width - space_ship_width  :
        red.x += 5
    if keys[pygame.K_LEFT] and red.x - 5 > width//2 :
        red.x -= 5
    if keys[pygame.K_DOWN] and  red.y + 5 < height - space_ship_height :
        red.y += 5
    if keys[pygame.K_UP] and red.y - 5 > 0 :
        red.y -= 5
def handel_bullets(yellow_bullet, red_bullet, yellow, red):
    for bull in yellow_bullet:
            bull.x += 7
            if red.colliderect(bull):
                pygame.event.post(pygame.event.Event(red_hit))
                yellow_bullet.remove(bull)
            elif bull.x > width:
                yellow_bullet.remove(bull)
                
    for bul in red_bullet:
        bul.x -= 7
        if yellow.colliderect(bul):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullet.remove(bul)
        elif bul.x < 0:
            red_bullet.remove(bul)
        


    
#define runing game

def draw_winners(text):
    wt=winner_font.render(text, 1, (155,200,200))    
    win.blit(wt,(width//2,height//2))
    pygame.display.update()
    pygame.time.delay(6000)


def main():
    red=pygame.Rect(width-(width//8), height//2, space_ship_width, space_ship_height)
    yellow=pygame.Rect(width//8, height//2, space_ship_width, space_ship_height)
    
    clock=pygame.time.Clock()
    red_bullet=[]
    yellow_bullet=[]
    red_health = 10
    yellow_helath = 10
    
    run=True
    
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullet) < max_bullets:
                    bullet_yellow = pygame.Rect(yellow.x + yellow.width , yellow.y + yellow.height//2 - 2 , 10,5 )
                    yellow_bullet.append(bullet_yellow)
                    bullet_fire_sound.play()
                    
                if event.key == pygame.K_RCTRL and len(red_bullet) < max_bullets:
                    bullet_red = pygame.Rect(red.x - red.width , red.y + red.height//2 - 2 , 10,5 )
                    red_bullet.append(bullet_red)
                    bullet_fire_sound.play()
            if event.type == red_hit:
                red_health -= 1
                bullet_hit_sound.play()
            if event.type == yellow_hit:
                bullet_hit_sound.play()
                yellow_helath -= 1
        win_text=''
        if red_health <= 0:
            win_text = 'YELLOW WINS'
           
        if yellow_helath <= 0:
            win_text = 'RED WINS'
           
        if win_text != '':
            draw_winners(win_text)
            break
        #movment 
        
        keys=pygame.key.get_pressed()
        yellow_movment(keys, yellow)
        red_movment(keys, red)
        handel_bullets(yellow_bullet,red_bullet,yellow,red)
        draw(yellow,red,red_bullet, yellow_bullet,red_health,yellow_helath)      
          
        
    
    
if __name__ == '__main__':
    main()
    





