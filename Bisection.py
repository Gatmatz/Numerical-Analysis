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


def Bisection(a, b, error):
    if f(a) * f(b) < 0:  # if Bolzano is valid
        counter = 0  # Initialize the iteration counter
        while abs(b - a) > error:  # while the precision is smaller than 5 digits
            c = (a + b) / 2  # take the middle of a and b
            print(counter, c)
            if f(c) == 0:  # if c is root then stop
                return c
            counter = counter + 1
            if f(a) * f(c) < 0:  # If the root is to the left of the middle
                b = c  # make the end of the space to the middle
            else:  # If the root is to the right of the middle
                a = c  # make the start of the space to the middle
        return c
    else:  # if Bolzano is not valid
        print('Bisection method failed')
        return None

# plotFunction()
error = 0.5 * (10 ** (-5))
# results = Bisection(0, 1, error)
# results = Bisection(1.5, 3, error)
# if results is not None:
#     print('Root:', round(results, 5))
#     print('f(Root):', round(f(results), 5))
# else:
#     print('Error')