import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as smp


def f(x):
    return 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * pow(x, 3) + 20 * pow(x, 2) - 26 * x + 12


def firstder(x):
    return 14 * x * np.exp(x - 2) + 2 * np.exp(x - 2) - 21 * x ** 2 + 40 * x - 26


def secondder(x):
    return 14 * x * np.exp(x - 2) + 16 * np.exp(x - 2) - 42 * x + 40


def plotFunction():
    # Plot equation for [0,3] with 100 samples
    x = np.linspace(0, 3, 100)
    y = f(x)
    figure1 = plt.figure()
    ax = figure1.add_subplot(1, 1, 1)
    ax.set_xlim([0, 3])
    ax.set_ylim([-2, 10])
    ax.axhline(linewidth=1, color='red')
    ax.axvline(linewidth=1, color='red')
    plt.title('Plot of f(x)')
    plt.grid(color='black', linestyle='--', linewidth=0.5)
    plt.plot(x, f(x), 'blue', linewidth=1.5)  # Plot function with given color
    plt.show()
    return

def Secant(x0, x1, error):
    if f(x1) - f(x0) == 0:  # if the the denominator is zero
        print('Division by zero!')
        return None  # Secant method fails
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    counter = 0  # initialize the iteration counter
    while abs(x2 - x1) > error:  # while the precision is smaller than 5 digits
        if f(x2) == 0:  # if new value x(n+1) is root
            return x1  # return the root
        print(counter, x2)  # print the current iteration and root approximation
        x0 = x1  # set the next value for x(n-1)
        x1 = x2  # set the next value for x(n)
        if f(x1) - f(x0) == 0:  # if the the denominator is zero
            print('Division by zero!')
            return None  # Secant method fails
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))  # set the next value for x(n+1)
        counter = counter + 1  # increase the iteration counter by one
    return x2  # return the approximate root

# plotFunction()
# results = Secant(0, 1, error)
# results = Secant(1.5, 2.5, error)
# if results is not None:
#     print('Root:', round(results, 5))
#     print('f(Root):', round(f(results), 5))
# else:
#     print('Error')