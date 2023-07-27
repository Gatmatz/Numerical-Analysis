def ModdedSecant(x0, x1, x2, error):
    if f(x0) == 0:  # if one of the initial estimates are root of the function
        return x0  # return the root x0
    elif f(x1) == 0:
        return x1  # return the root x1
    elif f(x2) == 0:
        return x2  # return the root x2
    q = f(x0) / f(x1)  # initialize q with the initial estimates
    r = f(x2) / f(x1)  # initialize r with the initial estimates
    s = f(x2) / f(x0)  # initialize s with the initial estimates
    if (q - 1) == 0 or (r - 1) == 0 or (s - 1) == 0:  # if the the denominator is zero
        print('Division by zero!')
        return None  # Secant method fails
    x3 = x2 - (r * (r - q) * (x2 - x1) + (1 - r) * s * (x2 - x0)) / (
            (q - 1) * (r - 1) * (s - 1))  # calculate the modified recursive method
    counter = 0  # initialize the iteration counter
    while abs(x3 - x2) > error:  # while the precision is smaller than 5 digits
        if f(x3) == 0:  # if new value x(n+3) is root
            return x1  # return the root x(n+3)
        print(counter, x3)  # print the current iteration and root approximation
        x0 = x1  # set the next value for x(n)
        x1 = x2  # set the next value for x(n+1)
        x2 = x3  # set the next value for x(n+2)
        if f(x0) == 0:  # if x(n) is root
            return x0  # return the root
        elif f(x1) == 0:  # if x(n+1) is root
            return x1  # return the root
        elif f(x2) == 0:  # if x(n+2) is root
            return x2  # return the root
        q = f(x0) / f(x1)  # calculate q with the new values
        r = f(x2) / f(x1)  # calculate r with the new values
        s = f(x2) / f(x0)  # calculate s with the new values
        if (q - 1) == 0 or (r - 1) == 0 or (s - 1) == 0:  # if the the denominator is zero
            print('Division by zero!')
            return None  # Secant method fails
        x3 = x2 - (r * (r - q) * (x2 - x1) + (1 - r) * s * (x2 - x0)) / (
                (q - 1) * (r - 1) * (s - 1))  # set the next value for x(n+3)
        counter = counter + 1  # increase the iteration counter by one
    return x3  # return the approximate root


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


#plotFunction()
error = 0.5 * (10 ** (-5))
# results = ModdedSecant(-2, -1.75, -1.5, error)
# results = ModdedSecant(-1, -0.75, 0, error)
# results = ModdedSecant(0, 0.25, 0.4, error)
# results = ModdedSecant(0.3, 0.55, 0.75, error)
# results = ModdedSecant(1, 1.5, 2, error)
# if results is not None:
#     print('Root:', round(results, 5))
#     print('f(Root):', round(f(results), 5))
# else:
#     print('Error')