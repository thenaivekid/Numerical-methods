#include <iostream>
#include <vector>

using namespace std;

void printMatrix(const vector<vector<double>>& matrix) {
    for (const auto& row : matrix) {
        for (double val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
}

void gaussianJordanNormalForm(vector<vector<double>>& A) {
    int n = A.size();
    for (int j = 0; j < n; ++j) {
        // Handling zero pivot element by swapping rows
        if (A[j][j] == 0) {
            for (int i = j + 1; i < n; ++i) {
                if (A[i][j] != 0) {
                    swap(A[j], A[i]);
                    break;
                }
            }
        }

        double pivot = A[j][j];
        for (int i = 0; i < n; ++i) {
            if (i != j) {
                double ratio = A[i][j] / pivot;
                for (int k = 0; k < n * 2; ++k) {
                    A[i][k] -= ratio * A[j][k];
                }
            }
        }
    }

    // Normalize each row
    for (int i = 0; i < n; ++i) {
        double pivot = A[i][i];
        for (int j = 0; j < n * 2; ++j) {
            A[i][j] /= pivot;
        }
    }
}

vector<vector<double>> matrixInverse(const vector<vector<double>>& matrix) {
    int n = matrix.size();
    // Create an augmented matrix [matrix | I]
    vector<vector<double>> A(n, vector<double>(n * 2, 0.0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            A[i][j] = matrix[i][j];
        }
        A[i][i + n] = 1.0;
    }

    // Apply Gaussian-Jordan elimination
    gaussianJordanNormalForm(A);

    // Extract the inverse matrix from the augmented matrix
    vector<vector<double>> inverseMatrix(n, vector<double>(n, 0.0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            inverseMatrix[i][j] = A[i][j + n];
        }
    }

    return inverseMatrix;
}

int main() {
    // Example usage
    vector<vector<double>> matrix = {{1, -1, 2}, {1, 2, 3}, {3, -4, -5}};
    auto inverseMatrixResult = matrixInverse(matrix);

    if (!inverseMatrixResult.empty()) {
        cout << "Inverse Matrix:" << endl;
        printMatrix(inverseMatrixResult);
    }

    return 0;
}
