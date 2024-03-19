import numpy as np


def fun(x):
    return (np.exp(x) + np.sin(x)) / (1 + x**2)


# fun = lambda x: x**2

x0 = 0
for i in range(0, 5):
    print(fun(i * 0.5 + x0))


def trapezoidal(a, b, n):
    h = (b - a) / n
    res = fun(a) + fun(b)
    for i in range(1, n):
        res += 2 * fun(a + i * h)
    res *= h / 2
    return res


print("integration: ", trapezoidal(0, 2, 4 * 2 * 2))
