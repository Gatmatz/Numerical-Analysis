import matplotlib.pyplot as plt
import numpy as np
import random


def f(x):
    return 54 * pow(x, 6) + 45 * pow(x, 5) - 102 * pow(x, 4) - 69 * pow(x, 3) + 35 * pow(x, 2) + 16 * x - 4


def firstder(x):
    return 324 * pow(x, 5) + 225 * pow(x, 4) - 408 * pow(x, 3) - 207 * pow(x, 2) + 70 * x + 16


def secondder(x):
    return 1620 * pow(x, 4) + 900 * pow(x, 3) - 1224 * pow(x, 2) - 414 * x + 70


def plotFunction():
    # Plot equation for [-2,2] with 100 samples
    x = np.linspace(-2, 2, 100)
    y = f(x)
    figure1 = plt.figure()
    ax = figure1.add_subplot(1, 1, 1)
    ax.set_xlim([-2, 2])
    ax.set_ylim([-30, 30])
    ax.axhline(linewidth=0.75, color='red')
    ax.axvline(linewidth=0.75, color='red')
    plt.title('Plot of f(x)')
    plt.grid(color='black', linestyle='--', linewidth=0.5)
    plt.plot(x, f(x), 'blue', linewidth=1.5)  # Plot function with given color
    plt.show()
    return

def ModdedBisection(a, b, error):
    if f(a) * f(b) < 0:  # if Bolzano is valid
        counter = 0  # Initialize the iteration counter
        while abs(b - a) > error:  # while the precision is smaller than 5 digits
            c = random.uniform(a, b)  # take a random float in the range of a and b
            print(counter, c)
            if f(c) == 0:  # if c is root then stop
                return c
            counter = counter + 1
            if f(a) * f(c) < 0:  # If the root is to the left of the random number
                b = c  # make the end of the space to the random number
            else:  # If the root is to the right of the random number
                a = c  # make the start of the space to the random number
        return c
    else:  # if Bolzano is not valid
        print('Bisection method failed')
        return None


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

#plotFunction()
error = 0.5 * (10 ** (-5))
# results = ModdedBisection(-2, -1, error)
# results = ModdedBisection(0, 0.4, error)
# results = ModdedBisection(0.4, 0.6, error)
# results = ModdedBisection(1, 2, error)