# To find the approximate value of the root of a polynomial using the Bisection method, implemented from 
# scratch without using any pre-built modules.

def function(x):
    return x**3 - x - 2

def bisection(a,b,tol=0.0001)