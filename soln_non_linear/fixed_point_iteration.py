import numpy as np
def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    """
    Finds the root of a function f using the Fixed-Point Iteration method.

    Args:
      g: The function used for iteration, of the form x = g(x).
      x0: Initial guess for the root.
      tol: Tolerance for the root approximation.
      max_iter: Maximum number of iterations.

    Returns:
      The approximate root of the function or None if not found.
    """

    for i in range(max_iter):
        x_n = g(x0)
        if abs(x_n - x0) < tol:
            print(f"converged after {i} iterations")
            return x_n
        x0 = x_n
    return None


# Example usage: Find the root of f(x) = sin(x) - x
f = lambda x: x**2 - x - 1
g = lambda x: 1 / (x - 1) # g(x) = x + f(x)
g = lambda x: (-np.sin(x) + 2)/3

# Find the root
root = fixed_point_iteration(g, 0)  # Adjust initial guess as needed

# Print the result
print(f"Root (Fixed-Point Iteration): {root}")
