def func(x, a, b, c):
    return a*x**2 + b*x + c

def func_tabel(a, b, c):
    bawah = float(input("Masukkan batas bawah: "))
    atas = float(input("Masukkan batas atas: "))
    err = float(input("Masukkan error: "))
    n = int(input("Masukkan n: "))
    hasil = 0
    i = 1
    e = 100
    h = abs(atas+bawah)/n
    x = bawah
    while i<=n:
        fx1 = func(x, a, b, c)
        fx2 = func(x+1*h, a, b, c)
        if (fx1*fx2 <= 0):
            if abs(fx1) < abs(fx2):
                hasil = x
                break
            else:
                hasil = x+h
                break
        #print("i = " + str(i-1))
        #print("x = " + str(x))
        #print("fx1 = " + str(fx1))
        #print("fx2 = " + str(fx2))
        #print("------------------")
        x = x+1*h
        i+=1
    return hasil