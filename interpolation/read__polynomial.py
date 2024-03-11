import numpy as np


def polynomial_curve_fit(x, y, degree):
    n = len(x)

    # Check if there are enough data points for the chosen degree
    if n < degree:
        print("Insufficient number of data points.")
        return None

    # Initialize the coefficients matrix
    a = np.zeros((degree + 1, degree + 2))

    # Populate the coefficients matrix
    for i in range(degree + 1):
        for j in range(degree + 1):
            a[i][j] = np.sum(x ** (i + j))

    # Populate the right-hand side of the matrix
    for i in range(degree + 1):
        a[i][degree + 1] = np.sum((x**i) * y)

    # Display the augmented matrix
    print("\nAugmented matrix:")
    print(a)

    # Gauss Jordan Method
    for j in range(degree + 1):
        if np.abs(a[j][j]) < 0.0001:
            print("Error: Pivot element is zero.")
            return None

        for i in range(degree + 1):
            if i != j:
                ratio = a[i][j] / a[j][j]
                a[i, j:] -= ratio * a[j, j:]

    # Solutions
    print("\nThe solution is:")
    coefficients = []
    for i in range(degree + 1):
        ans = a[i, degree + 1] / a[i, i]
        if np.abs(ans) < 0.000001:
            ans = 0
        coefficients.append(ans)
        print(f"{chr(ord('a') + i)} = {ans}")

    return coefficients


# Example usage
x_values = np.array([1, 2, 3, 4, 5, 6])
y_values = np.array([1, 4, 9, 16, 25, 36])
degree_of_polynomial = 2

# Call the function for polynomial curve fitting
coefficients = polynomial_curve_fit(x_values, y_values, degree_of_polynomial)
