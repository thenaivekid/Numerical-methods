// Online C++ compiler to run C++ program online
#include <iostream>
#include <cmath>
using namespace std;

void print_mat(float a[][10], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n + 1; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    float a[10][10];
    int n;
    cout << "enter order of matrix: " << endl;
    cin >> n;
    cout << "enter elements of augmented matrix: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n + 1; j++)
        {
            cin >> a[i][j];
        }
    }

    print_mat(a, n);
    cout << endl;

    for (int j = 0; j < n - 1; j++)
    {
        for (int i = j + 1; i < n; i++)
        {
            if (fabs(a[j][j] < 0.0004))
            {
                cout << a[j][j];
                cerr << "  division by zero";
                return -1;
            }
            float ratio = a[i][j] / a[j][j];
            for (int k = 0; k < n + 1; k++)
            {
                a[i][k] -= ratio * a[j][k];
            }
        }
    }

    print_mat(a, n);
    cout << endl;

    float solution[n] = {0};
    for (int i = n - 1; i >= 0; i--)
    {
        float sum = 0;
        for (int j = 0; j < n; j++)
        {
            sum += a[i][j] * solution[j];
        }
        solution[i] = (a[i][n] - sum) / a[i][i];
    }

    cout << "soln: ";
    for (int i = 0; i < n; i++)
    {
        cout << solution[i] << " ";
    }
    return 0;
}
// 4 1 1 3 2 12 2 1 1 4 11 10 2 -4 1 3 5 8 -3 2 -3
// 4 2 1 - 1 2 8 4 - 2 1 3 1 - 2 1 - 2 - 3 -3 1 - 1 2 - 1 4
//  3 5 0 2 7 1 3 4 8 2 1 2 5
// 3 3 2 3 18 1 4 9 16 2 1 1 10
// 3 1 -1 2 3 1 2 3 5 3 -4 -5 -13