import time

pikachu = time.gmtime(time.time())
print('hour : ' , (pikachu.tm_hour+9))
print('min : ' , pikachu.tm_min)
print('sec : ' , pikachu.tm_sec)

