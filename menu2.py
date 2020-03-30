from tabel import *
from biseksi import *
from regula import *
from iterasi import *
from newton import *
from secant import *

def pilihan(a, b, c, pil):
    if (pil == "1"):
        print("Metode Tabel")
        tabel(a, b, c)
    elif (pil == "2"):
        print("Metode biseksi")
        biseksi(a, b, c)
    elif (pil == "3"):
        print("Metode regula falsi")
        regula(a, b, c)
    elif (pil == "4"):
        print("Metode Newton Raphson")
        newton(a, b, c)
    elif (pil == "5"):
        print("Metode Secant")
        secant(a, b, c)