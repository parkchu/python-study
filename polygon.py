import turtle as t



n = 3
t.color('yellow')
t.begin_fill()
for x in range(n):
    t.forward(50)
    t.left(360/n)
t.end_fill()
