import turtle as t


def turn_right():
    t.setheading(0)
    t.forward(10)

def trun_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()

t.shape('turtle')
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(trun_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, 'Escape')
t.listen()
