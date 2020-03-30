from tabel import *
from biseksi import *
from regula import *
from iterasi import *
from newton import *
from secant import *
from grafik import *

a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
c = float(input("Masukkan c: "))
#grafik_kuadrat(a, b, c)
print("1. Metode Tabel\n2. Metode Biseksi\n3. Metode Regula Falsi\n4. Metode Iterasi\n5. Metode Newton Raphson\n6. Metode Secant")
pil = input("masukkan pilihan: ")
if (pil == "1"):
    print("Metode Tabel")
    print(func_tabel(a, b, c))
elif (pil == "2"):
    print("Metode biseksi")
    print(func_biseksi(a, b, c))
elif (pil == "3"):
    print("Metode regula falsi")
    print(func_regula(a, b, c))
elif (pil == "4"):
    print("Metode iterasi")
    print(func_iterasi(a, b, c))
elif (pil == "5"):
    print("Metode Newton Raphson")
    print(func_newton(a, b, c))
elif (pil == "6"):
    print("Metode Secant")
    print(func_secant(a, b, c))