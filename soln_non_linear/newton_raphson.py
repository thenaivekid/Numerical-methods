import numpy as np


def f(x):
    return np.sin(x) - 1 / x


def df(x):
    # Derivative of f(x) with respect to x
    return np.cos(x) + 1 / (x**2)


def newton_raphson(initial_guess, tol=1e-6, max_iter=100):
    x = initial_guess
    iteration = 0

    while abs(f(x)) > tol and iteration < max_iter:
        x = x - f(x) / df(x)
        iteration += 1

    if iteration == max_iter:
        print(
            "Newton-Raphson method did not converge within the specified number of iterations."
        )
    else:
        print(f"Root found at x = {x} after {iteration} iterations.")


# Provide an initial guess
initial_guess = 1.0

# Call the Newton-Raphson method
newton_raphson(initial_guess)
