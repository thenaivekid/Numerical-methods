import numpy as np

f = lambda x,y: x + y

tolerance = 1e-6
x0 = 0
y0 = 0
h = 0.2
xn = 1
n = (xn - x0) / h
for _ in range(int(n)):
    yn = y0+ h*f(x0, y0)
    print(x0, " next y ", yn)
    x0 += h
    y0 = yn
    
print(f"answer is {yn}")