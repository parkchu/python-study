import turtle as t
t.speed(1000)
t.pensize(3)
b = 90
t.seth(b)
t.fd(250)
t.ht()

def f(degree):
    t.pensize(3)
    t.color('black')
    t.seth(degree)
    t.fd(250)
    t.clear()
    t.reset()

def drawMinute(degree):
    newMinute = t.Turtle()
    newMinute.ht()
    newMinute.speed(1000)
    newMinute.color('black')
    newMinute.seth(b - degree)
    newMinute.fd(200)
    newMinute.back(200)
    return newMinute

y = 0
newMinute = None
for x in range(0,1000):
    if x % 10 == 0:
        if newMinute != None:
            newMinute.clear()
            newMinute.reset()
        newMinute = drawMinute(6 * y)
        y = y + 1


    t.ontimer(f(90 - x * 6), 10)

       
        
        


