import matplotlib.pyplot as plt
import numpy

def func(x, a, b, c):
    return a*x**2 + b*x + c

def func_secant(a, b, c):
    x0 = int(input("Masukkan batas bawah: "))
    x1 = int(input("Masukkan batas atas: "))
    err = float(input("Masukkan error: "))
    n = int(input("Masukkan n: "))
    i = 1
    e = 100

    while (e>err):
        y0 = func(x0, a, b, c)
        y1 = func(x1, a, b, c)
        x2 = x1 - y1 * ((x1 - x0) / (y1 - y0))
        y2 = func(x2, a, b, c)
        e = abs(y2)
        print("x0: %6.4f x1: %6.4f x2: %6.4f f(x1): %6.4f f(x2): %6.4f f(x3): %6.4f " % (x0, x1, x2, y0, y1, y2))
        if e > err:
            x0 = x1
            x1 = x2
    return x2