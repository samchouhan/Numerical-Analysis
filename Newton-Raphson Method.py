#To find the approximate value of the root of a polynomial using the Newton-Raphson method.
from scipy.optimize import newton

def function(x):
    return x**2 - 4

def df(x):
    return 2*x

# Find the root using the Newton-Raphson method
root = newton(function, 1, fprime=df)
print(f"The approximate value of the root is: {root}")