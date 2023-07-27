import math
from copy import deepcopy
import numpy as np

def buildMatrices(n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = 5
    for i in range(n - 1):
        A[i + 1][i] = -2
        A[i][i + 1] = -2

    b = np.zeros(n)
    b[0] = 3
    b[n - 1] = 3
    for i in range(1, n - 1):
        b[i] = 1

    return A, b


def infNorm(A):
    max = 0
    if len(A.shape) == 1:
        for i in range(len(A)):
            if A[i] > max:
                max = A[i]
    else:
        for i in range(len(A)):
            sum = 0
            for j in range(len(A[0])):
                sum += abs(A[i][j])
            if sum > max:
                max = sum

    return max


def GaussSeidel(n):
    # Make a tuple including matrices A and b
    tmp = buildMatrices(n)
    # Build A and b respectfully
    A = tmp[0]
    b = tmp[1]
    # Initiate 2 starting vectors
    x0 = np.zeros(n)
    x1 = np.zeros(n)
    while 1:
        # Calculate new vertor x1 according to the modded GaussSeidel Formula
        for i in range(n):
            x1[i] = b[i]
            if i == 0:
                x1[i] -= A[i][i + 1] * x0[i + 1]
            elif i == n - 1:
                x1[i] -= A[i][i - 1] * x1[i - 1]
            else:
                x1[i] -= A[i][i - 1] * x1[i - 1]
                x1[i] -= A[i][i + 1] * x0[i + 1]
            x1[i] = x1[i] / A[i][i]
        if abs(infNorm(x1) - infNorm(x0)) < 0.5 * pow(10, -4):  # Terminal condition
            return x1
        else:
            # Copy vector x1 to x0
            x0 = deepcopy(x1)
# print('Gauss-Seidel for n=10')
# x = GaussSeidel(10)
# print(x)
#
# print('Gauss-Seidel for n=10000')
# x = GaussSeidel(10000)
# print(x)