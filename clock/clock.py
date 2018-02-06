import turtle as t
import time

chu = time.gmtime(time.time())

t.speed(1000)
t.pensize(1)
b = 90
t.seth(b)
t.ht()

cir = t.Turtle()
cir.speed(1000)
cir.ht()
cir.color('white')
cir.sety(-300)
cir.color('black')
cir.circle(300)
cir.color('white')


def drawline(pikachu, pichu):
    cir.goto(0,0)
    cir.seth(b - pikachu)
    cir.fd(300)
    cir.color('black')
    cir.back(pichu)
    cir.color('white')
for h in range(1,61):
    if h % 5 == 0:
        cir.pensize(5)
        drawline(h * 6, 40)
        
    else:
        cir.pensize(3)
        drawline(h * 6, 20)
     

def f(degree):
    t.clear()
    t.reset()
    t.speed(1000)
    t.ht()
    t.pensize(1)
    t.color('black')
    t.seth(degree)
    t.fd(250)
    
def drawMinute(degree):
    newMinute = t.Turtle()
    newMinute.ht()
    newMinute.pensize(3)
    newMinute.speed(1000)
    newMinute.color('black')
    newMinute.seth(b - degree)
    newMinute.fd(200)
    newMinute.back(200)
    return newMinute

def drawhour(pikachu):
    hour = t.Turtle()
    hour.ht()
    hour.pensize(5)
    hour.speed(1000)
    hour.color('black')
    hour.seth(b - pikachu)
    hour.fd(150)
    hour.back(150)
    return hour

c = 1000
a = 100
y = 0
k = 0
hour = None
newMinute = None
while True:
    for x in range(0,3600):
        chu = time.gmtime(time.time())
        if chu.tm_sec <= c:
            chu = time.gmtime(time.time())
            c = 0
            if newMinute != None:
                newMinute.clear()
                newMinute.reset()
            newMinute = drawMinute(6 * chu.tm_min)
            y = y + 1
            if chu.tm_min <= a:
                chu = time.gmtime(time.time())
                a = 0
                if hour != None:
                    hour.clear()
                    hour.reset()
                hour = drawhour(30 * (chu.tm_hour + 9))
                k = k + 1

        t.ontimer(f(90 - chu.tm_sec * 6), 850)

       
