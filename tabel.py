import matplotlib.pyplot as plt
import numpy

a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
c = int(input("Masukkan c: "))

def func(x):
    return a*x**2 + b*x + c

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
err = float(input("Masukkan error: "))
n = int(input("Masukkan n: "))
hasil = 0
i = 1
e = 100
h = abs(atas+bawah)/n
x = bawah
while i<=n:
    fx1 = func(x)
    fx2 = func(x+1*h)
    if (fx1*fx2 <= 0):
        hasil = x
        break
    x = x+1*h
    print("i = " + str(i-1))
    print("x = " + str(x))
    print("fx1 = " + str(fx1))
    print("fx2 = " + str(fx2))
    print("------------------")
    i+=1
print("hasil = " +str(hasil))