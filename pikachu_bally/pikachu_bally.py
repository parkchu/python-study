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
        if self.rect.left < 0 or self.rect.right > 1034:
            self.speed[0] = - self.speed[0]
        if self.rect.bottom >= 625 - 65:
            self.speed[1] = self.speed[1] * 0
            a = 0
            return a
        if joohan == 0:
            if self.rect.top < 0:
                self.speed[1] = - self.speed[1]

pygame.init()
screen = pygame.display.set_mode([1034,625])
screen.fill([255,255,255])

speed = [0,0]
location = 0,0
background = Pikachu(speed, location, 'background.png')

speed = [0,0]
location = 1034/2 - 25, 650 - 290
stick = Pikachu(speed, location, 'stickbody.png')

speed = [0,0]
location = 1034/2 - 25, 650 - 315
stickhead = Pikachu(speed, location, 'sticktop.png')

speed = [0,0]
location = 100, 625 - 240
left = Pikachu(speed, location, 'leftpikachu.png')

speed = [0,0]
location = 1034 - 242, 625 - 240
right = Pikachu(speed, location, 'rightpikachu.png')

speed = [0,0]
location = 0, 625 - 500
jump = Pikachu(speed, location, 'jump.png')

speed = [0, 5]
location = 100, - 50
monsterball = Pikachu(speed, location, 'monsterball.png')

screen.blit(background.image, background.rect)
screen.blit(stick.image, stick.rect)
screen.blit(left.image, left.rect)
screen.blit(right.image, right.rect)
screen.blit(jump.image, jump.rect)
screen.blit(monsterball.image, monsterball.rect)
screen.blit(stickhead.image, stickhead.rect)

pygame.display.flip()
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)
joohan = 1

while True:
    screen.blit(background.image, background.rect)
    screen.blit(stick.image, stick.rect)
    screen.blit(stickhead.image, stickhead.rect)
    a = right.move()
    b = left.move()
    monsterball.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if a == 0:
                    right.speed[1] = -10
                    right.move()
                    a = 1
            if event.key == pygame.K_LEFT:
                right.speed[0] = - 5
                right.move()


            if event.key == pygame.K_RIGHT:
                right.speed[0] = 5
                right.move()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if b == 0:
                    left.speed[1] = -10
                    left.move()
                    b = 1
            if event.key == pygame.K_a:
                left.speed[0] = - 5
                left.move()

            if event.key == pygame.K_d:
                left.speed[0] = 5
                left.move()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                right.speed[0] = right.speed[0] * 0
                right.move()
            if event.key == pygame.K_RIGHT:
                right.speed[0] = right.speed[0] * 0
                right.move()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left.speed[0] =  0
                left.move()
            if event.key == pygame.K_d:
                left.speed[0] = 0
                left.move()

    if pygame.sprite.collide_rect(right, stick):
        right.speed[0] = 5

    if pygame.sprite.collide_rect(right, jump):
        right.speed[1] = 10

    if pygame.sprite.collide_rect(left, stick):
        left.speed[0] = - 5

    if pygame.sprite.collide_rect(left, jump):
        left.speed[1] = 10

    if pygame.sprite.collide_rect(monsterball, left):
        monsterball.speed[1] = - monsterball.speed[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                monsterball.speed[0] = monsterball.speed[0] - 1
            if event.key == pygame.K_d:
                monsterball.speed[0] = monsterball.speed[0] + 1

        joohan = 0

    if pygame.sprite.collide_rect(monsterball, right):
        monsterball.speed[1] = - monsterball.speed[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                monsterball.speed[0] = monsterball.speed[0] - 1
            if event.key == pygame.K_RIGHT:
                monsterball.speed[0] = monsterball.speed[0] + 1

        joohan = 0

    if pygame.sprite.collide_rect(monsterball, stickhead):
        monsterball.speed[1] = - monsterball.speed[1]
    if pygame.sprite.collide_rect(monsterball, stick):
        monsterball.speed[0] = - monsterball.speed[0]

    right.move()
    left.move()
    monsterball.move()
    screen.blit(monsterball.image, monsterball.rect)

    screen.blit(right.image, right.rect)
    screen.blit(left.image, left.rect)
    pygame.display.flip()


