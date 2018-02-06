import turtle as t

def draw(a):
    t.fd(100)
    t.lt(a)
b = 120
for x in range(7):
    draw(b)
    if x == 2:
        b = 90

t.circle(50)

    
