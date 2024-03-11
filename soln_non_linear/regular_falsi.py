import numpy as np


def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds the root of a function f using the Regular False Position method.

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
        x_r = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(x_r) < 0:
            b = x_r
        elif f(b) * f(x_r) < 0:
            a = x_r
        else:
            return x_r
        if abs(f(x_r)) < tol:
            print(f"converged after {i} iteration.")
            return x_r
    return None


# Example usage
f = lambda x: np.sin(x) - 1 / x + x
root = regula_falsi(f, 1, 2)
print(f"Root (Regular False Position): {root}")
