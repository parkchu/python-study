import pygame, sys


class Pikachu(pygame.sprite.Sprite):
    def __init__(self, speed, location, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
        self.location = location

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
def draw(speed, location, image_file):
    pika = Pikachu(speed, location, image_file)
    return pika

background = draw([0,0], (0,0), 'background.png')


speed = [0,0]
location = 1034/2 - 25, 650 - 290
stick = Pikachu(speed, location, 'stickbody.png')

speed = [0,0]
location = 1034/2 - 25, 650 - 315
stickhead = Pikachu(speed, location, 'sticktop.png')

speed = [0,0]
location = 100, 625 - 220
left = Pikachu(speed, location, 'leftpikachu.png')

speed = [0,0]
location = 1034 - 242, 625 - 220
right = Pikachu(speed, location, 'rightpikachu.png')

speed = [0,0]
location = 0, 625 - 480
jump = Pikachu(speed, location, 'jump.png')

speed = [0, 3]
location = 100, - 50
monsterball = Pikachu(speed, location, 'monsterball.png')

speed = [0, 0]
location =  0 - 25, 625 - 67
leftscore = Pikachu(speed, location, 'leftscore.png')

location = 1034/2 , 625 - 67
rightscore = Pikachu(speed, location, "rightscore.png")

score0 = draw([0,0], (0, 0), 'score.png')
rsco1 = draw([0,0], (0,0), 'score1.png')
rsco2 = draw([0,0], (0,0), 'score2.png')
rsco3 = draw([0,0], (0,0), 'score3.png')
lscore0 = draw([0,0], (1034 - 100, 0), 'score.png')
lsco1 = draw([0,0], (1034 - 100, 0), 'score1.png')
lsco2 = draw([0,0], (1034 - 100, 0), 'score2.png')
lsco3 = draw([0,0], (1034 - 100, 0), 'score3.png')


pygame.init()
screen = pygame.display.set_mode([1034,625])
screen.fill([255,255,255])

screen.blit(background.image, background.rect)
screen.blit(stick.image, stick.rect)
screen.blit(leftscore.image, leftscore.rect)
screen.blit(rightscore.image, rightscore.rect)
screen.blit(score0.image, score0.rect)
screen.blit(lscore0.image, lscore0.rect)
screen.blit(left.image, left.rect)
screen.blit(right.image, right.rect)
screen.blit(jump.image, jump.rect)
screen.blit(stickhead.image, stickhead.rect)
screen.blit(monsterball.image, monsterball.rect)


pygame.display.flip()
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)
joohan = 1
pikachu = 1
abc = 1
rig = 0
lef = 0

while True:

    screen.blit(background.image, background.rect)
    screen.blit(stick.image, stick.rect)
    screen.blit(stickhead.image, stickhead.rect)
    screen.blit(leftscore.image, leftscore.rect)
    screen.blit(rightscore.image, rightscore.rect)


    if rig == 0:
        screen.blit(score0.image, score0.rect)
    if rig == 1:
        screen.blit(rsco1.image, rsco1.rect)
    if rig == 2:
        screen.blit(rsco2.image, rsco2.rect)
    if rig == 3:
        screen.blit(rsco3.image, rsco3.rect)
    if lef == 0:
        screen.blit(lscore0.image, lscore0.rect)
    if lef == 1:
        screen.blit(lsco1.image, lsco1.rect)
    if lef == 2:
        screen.blit(lsco2.image, lsco2.rect)
    if lef == 3:
        screen.blit(lsco3.image, lsco3.rect)


    a = right.move()
    b = left.move()
    monsterball.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                abc = 1

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
            if event.key == pygame.K_f:
                pikachu = 1
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

        if pikachu == 1:

            monsterball.speed[1] = - monsterball.speed[1]

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_t:
                monsterball.speed[0] = 15
                monsterball.speed[1] = 5
                pikachu = 0
            if event.key == pygame.K_y:
                monsterball.speed[0] = 5
                monsterball.speed[1] = 15
                pikachu = 0
            if event.key == pygame.K_u:
                monsterball.speed[0] = 10
                monsterball.speed[1] = -10
                pikachu = 0



        joohan = 0

    if pygame.sprite.collide_rect(monsterball, right):

        if abc == 1:

            monsterball.speed[1] = - monsterball.speed[1]
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_i:
                monsterball.speed[0] = - 15
                monsterball.speed[1] = 5
                abc = 0
            if event.key == pygame.K_o:
                monsterball.speed[0] = - 5
                monsterball.speed[1] = 15
                abc = 0
            if event.key == pygame.K_p:
                monsterball.speed[0] = - 10
                monsterball.speed[1] = -10
                abc = 0


        joohan = 0

    if pygame.sprite.collide_rect(monsterball, stickhead):
        monsterball.speed[1] = - monsterball.speed[1]
    if pygame.sprite.collide_rect(monsterball, stick):
        monsterball.speed[0] = - monsterball.speed[0]
    if pygame.sprite.collide_rect(rightscore, monsterball):
        rig = rig + 1
        monsterball = draw([0,3], (1034 - 100 , - 50), 'monsterball.png')
        screen.blit(monsterball.image, monsterball.rect)
        pygame.display.flip()
        joohan = 1
    if pygame.sprite.collide_rect(leftscore, monsterball):
        lef = lef + 1
        monsterball = draw([0, 3], (100, - 50), 'monsterball.png')
        screen.blit(monsterball.image, monsterball.rect)
        pygame.display.flip()
        joohan = 1

    right.move()
    left.move()
    monsterball.move()
    screen.blit(monsterball.image, monsterball.rect)

    screen.blit(right.image, right.rect)
    screen.blit(left.image, left.rect)
    pygame.display.flip()


