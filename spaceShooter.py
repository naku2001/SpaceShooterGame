import pygame
import random
pygame.init()

pygame.display.set_mode((1000,700))
pygame.display.set_caption("SPACE SHOOTER GAME")
icon = pygame.image.load("launch.png")
background = pygame.image.load("space.jpg")
enemy = pygame.image.load("alien.png")

play= pygame.image.load("space.png")
DEFAULT_IMAGE_SIZE = (150, 150)
DEFAULT_ENEMY_SIZE = (60,60)
spaceShipX = 270
spaceShipY =  300 
changeX=0
alienSpeedX = -0.26


alienX = random.randint(0,736)
alienY = random.randint(30,150)
play = pygame.transform.scale(play,DEFAULT_IMAGE_SIZE)
enemy= pygame.transform.scale(enemy,DEFAULT_ENEMY_SIZE)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))



def player():
    screen.blit(play, (spaceShipX,spaceShipY))
    screen.blit(enemy,(alienX,alienY))
   



running = True
while running:
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX=-1  
            if event.key == pygame.K_RIGHT:
                changeX=1 
        if event.type == pygame.KEYUP:
            changeX=0        
    spaceShipX+=changeX 
    if spaceShipX<=0:
        spaceShipX=0
    elif spaceShipX>=720:
        spaceShipX = 720
      
    alienX+= alienSpeedX 
    if alienX <= 0:
        alienSpeedX=0.26
        alienY += 40
    if alienX >=720:
        alienSpeedX= -0.26
        alienY += 40     
  
        
                         
    player()        
    pygame.display.update()        
