import numpy as np


def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds the root of a function f using the Bisection method.

    Args:
      f: The function to find the root of.
      a: Lower bound of the initial interval.
      b: Upper bound of the initial interval.
      tol: Tolerance for the root approximation.
      max_iter: Maximum number of iterations.

    Returns:
      The approximate root of the function or None if not found.
    """
    for i in range(max_iter):
        x_m = (a + b) / 2
        if f(x_m) == 0 or abs(f(x_m)) < tol:
            print(f"converged after {i} iteration.")
            return x_m
        if f(a) * f(x_m) < 0:
            b = x_m
        else:
            a = x_m
    return None


# Example usage
f = lambda x: np.sin(x) - 1 / x
root = bisection_method(f, 1, 2)
print(f"Root (Bisection Method): {root}")
