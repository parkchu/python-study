import pygame, sys
from random import *

class myball(pygame.sprite.Sprite):
    def __init__(self,imgae_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.right = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = - self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.speed[1] = - self.speed[1]
            
class yourball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = - self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.speed[1] = - self.speed[1]

class anotherball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = - self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.speed[1] = - self.speed[1]

def balls(pikagroup, group):
    screen.fill([255,255,255])
    
    joohanball.move()
    screen.blit(joohanball.image, joohanball.rect)
    
    
    for pikachuball in pikagroup:
        pikachuball.move()
        screen.blit(pikachuball.image, pikachuball.rect)
        
        
    for anotherball in group:
        anotherball.move()
        screen.blit(anotherball.image, anotherball.rect)
    pygame.display.flip()        
    
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
image_file = ('beach_ball.png')
joohanball = myball(image_file, [0,0], [100,100])
pikachuball = yourball(image_file, [choice([-2,2]), choice([-2,2])], [200,200])
anotherball = anotherball(image_file, [choice([-2,2]), choice([-2,2])], [300,300])
pikagroup = pygame.sprite.Group()
pikagroup.add(pikachuball)
group = pygame.sprite.Group()
group.add(anotherball)

while True:
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif  event.type == pygame.MOUSEMOTION:
            joohanball.rect.center = event.pos
            
    
    
    
    balls(pikagroup, group)
    
    
    if pygame.sprite.spritecollide(joohanball, pikagroup, False):
        pikagroup.remove(pikachuball)
        
    if pygame.sprite.spritecollide(joohanball, group, False):
        group.remove(anotherball)
        
        
            
           
                
            
        
