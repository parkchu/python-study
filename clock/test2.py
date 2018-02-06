class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction


    def __str__(self):
        msg = 'hi, I am a ' + self.size +' '+self.color + ' ball!'
        return msg



myBall = Ball('red', 'small', 'down')
print(myBall)
