import time
from time import time

# t = int(time.time()) + 10800
t = int(time()) + 10800

h = t % 86400 // 3600
m = t % 3600 // 60
s = t % 60



print(f'{h}:{m}:{s}')
