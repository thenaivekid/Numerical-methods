import numpy as np

f = lambda x, y: x + y

tolerance = 1e-6
x0 = 0
y0 = 0
h = 0.2
xn = 1
n = (xn - x0) / h
for _ in range(int(n)):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + h/2, y0 + k1 /2)
    k3 = h * f(x0 + h/2, y0 + k2/2)
    k4 = h * f(x0 + h, y0 + k3)
    k = 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    yn = y0 + k
    print(x0, " next y ", yn)
    x0 += h
    y0 = yn

print(f"answer is {yn}")
