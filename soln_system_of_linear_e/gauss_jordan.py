import numpy as np

def gaussian_jordan(A):
    """
    Solves a system of linear equations using Gaussian elimination with row pivoting.

    Args:
        A: A 2D numpy array representing the augmented matrix.

    Returns:
        A numpy array containing the solution vector.
    """

    n = len(A)
    for j in range(n):
        if A[j][j] == 0:
            print("pivot element is zero")
            break
        for i in range(n):
            if i == j:
                continue
            ratio = A[i][j]/A[j][j]
            for k in range(n + 1):
                A[i][k] -= ratio*A[j][k]
    solution = [0]*n
    for i in range(n):
        solution[i] = A[i][n]/A[i][i]
    return solution


# Augmented matrix
A = [[1, -1, 2, 3], [1, 2, 3, 5], [3, -4, -5, -13]]

# Solve the system
solution = gaussian_jordan(A.copy())

# Print the solution
print("Solution:")
print(solution)
