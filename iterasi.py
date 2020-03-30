import math

def func(x, a, b, c):
    return a*x**2 + b*x + c

def gx(x, a, b, c):
    return math.sqrt((-1 * (b*x + c)) / a)

def func_iterasi(a, b, c):
    tebak = float(input("masukkan tebakan: "))
    err = float(input("Masukkan error: "))
    i = 1
    e = 100

    while (e>err):
        yx = gx(tebak, a, b, c)
        e = abs(tebak-yx)
        print('x: %6.4f f(x): %6.4f error: %6.4f ' % (tebak, yx, e))
        if abs(e) > err:
            tebak = yx
    return tebak
