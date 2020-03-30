def func(x, a, b, c):
    return a*x**2 + b*x + c

def func_biseksi(a, b, c):
    bawah = int(input("Masukkan batas bawah: "))
    atas = int(input("Masukkan batas atas: "))
    err = float(input("Masukkan error: "))
    n = int(input("Masukkan n: "))
    i = 1
    e = 100
    while i < n and abs(bawah-atas)>err:
        tengah = (atas + bawah)/2
        fa = func(atas, a, b, c)
        fb = func(bawah, a, b, c)
        fc = func(tengah, a, b, c)
        if fc*fa < 0:
            bawah = tengah
            fb = fc
        else:
            atas = tengah
            fa = fc
        i+=1
        print('a: %6.4f b: %6.4f c: %6.4f ya: %6.4f yb: %6.4f yc: %6.4f' %(atas, bawah, tengah, fa, fb, fc))
    return tengah

