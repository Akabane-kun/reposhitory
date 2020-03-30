import math

def func(x, a, b, c):
    return a*x**2 + b*x + c

def gx(x, a, b, c):
    return 2*a*x + b

def func_newton(a, b, c):
    tebak = float(input("masukkan tebakan: "))
    err = float(input("Masukkan error: "))
    i = 1
    e = 100

    while e>err:
        x1 = tebak - func(tebak, a, b, c)/gx(tebak, a, b, c)
        e = tebak-x1
        print("x: %6.4f f(x): %6.4f f'(x): %6.4f x1: %6.4f error: %6.4f " % (tebak, func(tebak, a, b, c), gx(tebak, a, b, c), x1, e))
        if e > err:
            tebak = x1
    return tebak