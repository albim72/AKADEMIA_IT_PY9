#n! = 1*2*..*n gdzie n -> liczba naturalna
#double 1.8E+308
#n????? double -> 171!

def silnia(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych")
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

try:
    n = int(input("podaj argument n silnii: "))
    print(f"silnia dla n = {n} wynosi: {silnia(n)}")
except ValueError as d:
    print(d)
