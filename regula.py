def func(x, a, b, c):
    return a*x**2 + b*x + c

def func_regula(a, b, c):
    bawah = float(input("Masukkan batas bawah: "))
    atas = float(input("Masukkan batas atas: "))
    err = float(input("Masukkan error: "))
    n = int(input("Masukkan n: "))
    i = 1
    e = 100

    fa = func(atas, a, b, c)
    fb = func(bawah, a, b, c)

    while i<=n and e>err:
        x = (fb*atas-fa*bawah)/(fb-fa)
        fx = func(x, a, b, c)
        e=abs(fx)
        if fx*fa<0:
            bawah = x
            fb = fx
        else:
            atas = x
            fa = fx
        i+=1
        print('bb: %6.4f ba: %6.4f x: %6.4f f(bb): %6.4f f(bb): %6.4f f(x): %6.4f' % (bawah, atas, x, fb, fa, fx))
    return x