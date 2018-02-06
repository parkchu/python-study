import turtle as t


t.speed(1000)
t.ht()
t.color('white')
t.sety(-300)
t.color('black')
t.circle(300)
t.color('white')
t.sety(300)
t.color('black')
t.pensize(3)
t.sety(300-20)
t.color('white')
t.goto(300,0)
t.color('black')
t.setx(300-20)
t.color('white')
t.goto(0,-300)
t.color('black')
t.sety(-300+20)
t.color('white')
t.goto(-300,0)
t.color('black')
t.setx(-300+20)
t.color('white')
t.goto(0,0)
t.color('black')
b = 90
t.seth(b)
t.fd(250)
t.ht()

minute = t.Turtle()
minute.speed(100)
minute.circle(100)



def f(degree):
    
    t.pensize(5)
    t.color('white')
    t.back(250)
    t.pensize(3)
    t.color('black')
    t.seth(degree)
    t.fd(250)



for x in range(1,60):

    t.ontimer(f(90 - x * 6), 1000)
    
    
    
    











