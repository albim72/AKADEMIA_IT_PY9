#n! = 1*2*..*n gdzie n -> liczba naturalna
#double 1.8E+308
#n????? double -> 171!
import sys
def silnia(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych")
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj argument n silnii: "))
    sys.setrecursionlimit(10000)
    print(f"silnia dla n = {n} wynosi: {silnia(n)}")
    print(f"silnia rekurencyjna dla n = {n} wynosi: {silnia_rek(n)}")
except ValueError as d:
    print(d)
