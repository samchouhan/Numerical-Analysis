# To find the approximate value of the root of a polynomial using the Bisection method, implemented from
# Scratch without using any pre-built modules.


def function(x):
    return x * x - 4


def bisection(a, b, tol=0.0001):
    if function(a) * function(b) >= 0:
        print("Bisection method fails.")
        return None

    while (b - a) >= tol:
        c = (a + b) / 2
        if function(c) == 0:
            break
        if function(a) * function(c) < 0:
            b = c
        else:
            a = c
    return c


root = bisection(1, 3)
print(f"The root is approximately: {root:.4f}")
