import numpy as np


def gaussian_elimination(A):
    """
    Solves a system of linear equations using Gaussian elimination with row pivoting.

    Args:
        A: A 2D numpy array representing the augmented matrix.

    Returns:
        A numpy array containing the solution vector.
    """

    n = len(A)
    for j in range(n - 1):
        # Check for zero pivot element
        if abs(A[j][j]) < 1e-6:
            print(
                "Warning: Pivot element is close to zero, solution may be inaccurate."
            )
            continue

        # Pivot row
        pivot_row = j

        # Find maximum element below the pivot in the current column
        for i in range(j + 1, n):
            if abs(A[i][j]) > abs(A[pivot_row][j]):
                pivot_row = i

        # Swap rows if necessary
        if pivot_row != j:
            A[j], A[pivot_row] = A[pivot_row], A[j]

        # Eliminate leading terms in subsequent rows
        for i in range(j + 1, n):
            ratio = A[i][j] / A[j][j]
            for k in range(n + 1):
                A[i][k] -= ratio * A[j][k]

    print(A)

    # Back-substitution
    solution = [0]*n
    for i in range(n-1, -1, -1):
        sum = 0
        for k in range(i+1, n):
            sum += A[i][k]*solution[k]
        solution[i] = (A[i][n] - sum)/A[i][i]
    return solution

    return solution


# Augmented matrix
A = [[1, -1, 2, 3], [1, 2, 3, 5], [3, -4, -5, -13]]
# Solve the system
solution = gaussian_elimination(A.copy())

# Print the solution
print("Solution:")
print(solution)
