def gaussian_jordan_normal_form(A):
    n = len(A)
    for j in range(n):
        # Handling zero pivot element by swapping rows
        if A[j][j] == 0:
            for i in range(j + 1, n):
                if A[i][j] != 0:
                    A[j], A[i] = A[i], A[j]
                    break
            else:
                print("Matrix is singular.")
                return None  # Matrix is singular, unable to find the inverse

        pivot = A[j][j]
        for i in range(n):
            if i != j:
                ratio = A[i][j] / pivot
                for k in range(n * 2):
                    A[i][k] -= ratio * A[j][k]

    # Normalize each row
    for i in range(n):
        pivot = A[i][i]
        for j in range(n * 2):
            A[i][j] /= pivot

    return A


def matrix_inverse(matrix):
    n = len(matrix)
    # Create an augmented matrix [matrix | I]
    A = [[0 for _ in range(n * 2)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = matrix[i][j]
        A[i][i + n] = 1

    # Apply Gaussian-Jordan elimination
    result = gaussian_jordan_normal_form(A)

    if result:
        # Extract the inverse matrix from the augmented matrix
        inverse_matrix = [[result[i][j + n] for j in range(n)] for i in range(n)]
        return inverse_matrix
    else:
        return None


# Example usage
matrix = [[1, -1, 2], [1, 2, 3], [3, -4, -5]]
inverse_matrix_result = matrix_inverse(matrix)

if inverse_matrix_result:
    print("Inverse Matrix:")
    for row in inverse_matrix_result:
        print(row)
