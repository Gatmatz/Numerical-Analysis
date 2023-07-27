import math
from copy import deepcopy
import numpy as np

def cholesky(A):
    # Check if matrix is symmetrical
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i != j:
                if A[i][j] != A[j][i]:
                    print('Matrix not symmetrical')
                    return None

    # Check if matrix is positively defined
    l = np.linalg.eigvals(A)
    for i in range(len(l)):
        if l[i] < 0:
            print('Matrix not positively defined')
            return None

    # Making a copy of matrix A
    L = np.zeros((len(A), len(A[0])))
    for i in range(len(A)):
        for j in range(len(A[0])):
            L[i][j] = A[i][j]  # Fill the U with the starting A matrix

    # Compute the lower-diagonal elements
    for i in range(len(L)):
        for k in range(0, i):
            L[i][i] -= np.dot(L[i][k], L[i][k])
        L[i][i] = math.sqrt(L[i][i])
        for j in range(i + 1, len(L)):
            for k in range(0, i):
                L[j][i] -= np.dot(L[j][k], L[i][k])
            L[j][i] /= L[i][i]

    # Make the upper-diagonal elements zero
    for i in range(0, len(L)):
        for j in range(0, len(L)):
            if j > i:
                L[i][j] = 0

    return L
    
# C = np.array([[4, -2, 2], [-2, 2, -4], [2, -4, 11]])
# L = cholesky(C)
# print(L)