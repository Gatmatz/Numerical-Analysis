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


def ModdedNewtonRaphson(x0, error):
    if firstder(x0) != 0 and f(x0) != 0 and (
            2 * pow(firstder(x0), 2) - f(x0) * secondder(x0)) != 0:  # if various denominators are zero
        x1 = x0 - 1 / ((firstder(x0) / f(x0)) - 0.5 * (
                secondder(x0) / firstder(x0)))  # initialise the recursive method with the initial estimates
        counter = 0  # Initialize the iteration counter
        while abs(x1 - x0) > error:  # while the precision is smaller than 5 digits
            if f(x1) == 0:  # if new value x(n+1) is root
                return x1  # then return the root
            print(counter, x1)  # print the current iteration and root approximation
            x0 = x1  # set the next value for x(n)
            if firstder(x0) == 0 or f(x0) == 0 or (2 * pow(firstder(x0), 2) - f(x0) * secondder(
                    x0)) == 0:  # if the denominator is zero
                print('Division by zero, Newton-Raphson fails!')
                return None  # NewtonRaphson method fails
            x1 = x0 - 1 / (
                    (firstder(x0) / f(x0)) - 0.5 * (secondder(x0) / firstder(x0)))  # set the next value for x(n+1)
            counter = counter + 1  # increase the iteration counter by one
        return x1  # return the approximate root
    else:
        print('Division by zero, Newton-Raphson fails!')
        return None


def NewtonRaphson(x0, error):
    if firstder(x0) != 0:
        x1 = x0 - f(x0) / firstder(x0)
        counter = 0  # Initialize the iteration counter
        while abs(x1 - x0) > error:  # while the precision is smaller than 5 digits
            if f(x1) == 0:  # if new value x(n) is root
                return x1  # then return the root
            print(counter, x1)  # print the current iteration and root approximation
            x0 = x1  # set the next values for x(n)
            if firstder(x0) == 0:  # if the derivative(hence the denominator) is zero
                print('Division by zero, Newton-Raphson fails!')
                return None  # NewtonRaphson method fails
            x1 = x0 - f(x0) / firstder(x0)  # and x(n+1)
            counter = counter + 1  # increase the iteration counter by one
        return x1  # return the approximate root
    else:
        print('Division by zero, Newton-Raphson fails!')
        return None

#plotFunction()
error = 0.5 * (10 ** (-5))
# results = ModdedNewtonRaphson(-2, error)
# results = ModdedNewtonRaphson(-1, error)
# results = ModdedNewtonRaphson(0, error)
# results = ModdedNewtonRaphson(0.6, error)
# results = ModdedNewtonRaphson(2, error)
# if results is not None:
#     print('Root:', round(results, 5))
#     print('f(Root):', round(f(results), 5))
# else:
#     print('Error')