import numpy as np
f = lambda x: np.sin(x) - 1 / x

g = lambda x: np.sin(x) - 1 / x + x


def secant_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds the root of a function f using the Secant method.

    Args:
      f: The function to find the root of.
      a, b: Initial guesses for the root, such that f(a) * f(b) < 0.
      tol: Tolerance for the root approximation.
      max_iter: Maximum number of iterations.

    Returns:
      The approximate root of the function or None if not found.
    """

    for i in range(max_iter):
        x_n = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(x_n)) < tol:
            print(f"converged after {i} iteration.")
            return x_n
        a, b = b, x_n
    return None


# Example usage
root = secant_method(g, 1, 2)
print(f"Root (Secant Method): {root}")
