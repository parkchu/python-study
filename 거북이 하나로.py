import turtle as t
t.speed(1000)
t.pensize(3)
b = 90
t.seth(b)
t.fd(250)
t.ht()


def f(degree):
    
    t.pensize(5)
    t.color('white')
    t.back(250)
    t.pensize(3)
    t.color('black')
    t.seth(degree)
    t.fd(250)



for x in range(1,61):

    t.ontimer(f(90 - x * 6), 1000)
