import random
import time

w = [ 'cat', 'dog', 'fox', 'monkey', 'panda', 'frog', 'snake', 'wolf', 'pikachu',]

n = 1
print('are you ready in game you press enter')
input()

start = time.time()


q = random.choice(w)
while n <= 5:
    print('*question', n)
    print(q)
    x = input()
    if q == x:
        print('good')
        n = n + 1
        q = random.choice(w)
    else:
        print('bad try again')


end = time.time()
et = end - start
et = format(et,'.2f')
print('time :', et, 'second')

    
