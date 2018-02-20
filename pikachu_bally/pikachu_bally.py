import pygame, sys


class Pikachu(pygame.sprite.Sprite):
    def __init__(self, speed, location, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = self.speed[0] * 0


pygame.init()
screen = pygame.display.set_mode([1034,625])
screen.fill([255,255,255])

speed = 0,0
location = 0,0
background = Pikachu(speed, location, 'background.png')

location = 1034/2 - 25, 625 - 290
stick = Pikachu(speed, location, 'stick.png')

location = 0, 625 - 240
left = Pikachu(speed, location, 'leftpikachu.png')

location = 1034 - 142, 625 - 240
right = Pikachu(speed, location, 'rightpikachu.png')

location = 0, 625 - 500
jump = Pikachu(speed, location, 'jump.png')

speed = 0, 0
location = 0, 0
monsterball = Pikachu(speed, location, 'monsterball.png')

screen.blit(background.image, background.rect)
screen.blit(stick.image, stick.rect)
screen.blit(left.image, left.rect)
screen.blit(right.image, right.rect)
screen.blit(jump.image, jump.rect)
screen.blit(monsterball.image, monsterball.rect)
pygame.display.flip()


while True:
    screen.blit(background.image, background.rect)
    screen.blit(stick.image, stick.rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right.speed[1] = right.speed[1] - 3
            if event.key == pygame.K_LEFT:
                right.speed[0] = right.speed[0] - 2
            if event.key == pygame.K_RIGHT:
                right.speed[0] = right.speed[0] + 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                right.speed[1] = right.speed[1] * 0
            if event.key == pygame.K_LEFT:
                right.speed[0] = right.speed[0] * 0
            if event.key == pygame.K_RIGHT:
                right.speed[0] = right.speed[0] * 0

        #    leftpikachu.move()

    monsterball.move()
    screen.blit(monsterball.image, monsterball.rect)
    right.move()
    screen.blit(right.image, right.rect)
    screen.blit(left.image, left.rect)
    pygame.display.flip()


