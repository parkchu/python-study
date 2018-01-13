import turtle as t
t.speed(1000)
t.pensize(3)
b = 90
t.seth(b)
t.fd(250)
t.ht()

a = t.Turtle()
a.seth(b)
a.ht()
a.speed(1000)
a.pensize(3)
a.color('black')

def f(degree):
    
    t.pensize(5)
    t.color('white')
    t.back(250)
    t.pensize(3)
    t.color('black')
    t.seth(degree)
    t.fd(250)



for x in range(1,61):
    if x == 60:
        a.color('black')
        a.seth(b - 6)
        a.fd(200)
        a.back(200)
    else:
        a.color('black')
        a.fd(200)
        a.back(200)

    t.ontimer(f(90 - x * 6), 1000)

       
        
        


