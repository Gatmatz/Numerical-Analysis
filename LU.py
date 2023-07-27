import math
from copy import deepcopy
import numpy as np


def swap(A, B):
    temp = np.zeros(len(A))
    for i in range(len(A)):
        temp[i] = A[i]

    for i in range(len(B)):
        A[i] = B[i]

    for i in range(len(A)):
        B[i] = temp[i]


def LU(A):
    # Initialize the P, L and U matrices
    P = np.zeros((len(A), len(A[0])))
    L = np.zeros((len(A), len(A[0])))
    U = np.zeros((len(A), len(A[0])))

    for i in range(len(A)):
        for j in range(len(A[0])):
            U[i][j] = A[i][j]  # Fill the U with the starting A matrix
            # Initialize the P matrix as a unit matrix
            if i != j:
                P[i][j] = 0
            else:
                P[i][j] = 1

    # Make the U matrix
    for j in range(len(U[0])):
        # Start the partial pivoting
        max = abs(U[j][j])
        max_index = j
        # Find the driver with the highest value in absolute value
        for i in range(j, len(U)):
            if abs(U[i][j]) > max:
                # Make the pivot - Swap rows
                swap(U[max_index], U[i])
                swap(P[max_index], P[i])
                swap(L[max_index], L[i])
                max = abs(U[i][j])  # set the new max value
                max_index = i  # set the new max index

        # Gauss forward elimination
        for i in range(0, len(U)):
            if i > j:
                if U[j][j] != 0:
                    L[i][j] = (U[i][j] / U[j][j])
                    U[i] = U[i] - (U[i][j] / U[j][j]) * U[j]
    # Give the diagonal elements of L the value 1
    for i in range(len(L)):
        L[i][i] = 1

    return P, L, U


def solveLU(A, b):
    if len(A) != len(b):
        print('System impossible or indefinite')
        return None
    P = LU(A)[0]
    L = LU(A)[1]
    U = LU(A)[2]

    # Take advantage of the partial pivoting in solving the system
    A = np.dot(P, A)
    b = np.dot(P, b)

    # Solve Ly=b
    y = []
    y = [0 for i in range(b.size)]
    for i in range(0, b.size):
        y[i] = b[i]
        for j in range(len(A[0])):
            if i > j:
                y[i] -= (L[i][j] * y[j])

    # Solve Ux=y
    x = []
    x = [0 for i in range(b.size)]
    for i in range(b.size - 1, -1, -1):
        x[i] = y[i]
        for j in range(b.size - 1, -1, -1):
            if j > i:
                x[i] -= (U[i][j] * x[j])
        if U[i][i] == 0:
            print('Division error! Method fails')
            return None
        else:
            x[i] /= U[i][i]

    return x

# A = np.array([[3, 1, -4, 1], [-5, 2, 1, -2], [-1, 6, -3, -4], [-2, 1, -4, 2]])
# b = np.array([1, -3, 2, 0])
# x = solveLU(A, b)
# if x is not None:
#     for i in range(len(x)):
#         print('x', i, '=', x[i])