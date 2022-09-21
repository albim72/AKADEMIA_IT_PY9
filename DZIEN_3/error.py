try:
    print(x)
except NameError:
    print("x nie istnieje!")
    x = float(input("podaj w takim razie x:"))
    if x == 0:
        wynik = "....."
    else:
        wynik = x*2
except:
    print("nieokreślony błąd")
finally:
    print(f"wynik x = {wynik}")
    y = float(input("podaj teraz drugą wartość y:"))
    print(f"y wynosi: {y}")

print("ciąg dalszy...")

print(f"wynik x = {wynik}")
print(y)
