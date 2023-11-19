import math

a = float(input("Введите строну a: "))
b = float(input("Введите строну b: "))

if 1001 > a > 0 and 1001 > b > 0:
    c = math.sqrt(a**2 + b**2)
    print(c)
else:
    print("a или b ,больше 1000 или меньше 0" )
