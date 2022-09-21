try:
    print(x)
except NameError:
    print("x nie istnieje!")
    x = float(input("podaj w takim razie x:"))
    print(f"x wynosi: {x}")
except:
    print("nieokreślony błąd")
finally:
    y = float(input("podaj teraz drugą wartość y:"))
    print(f"y wynosi: {y}")

print("ciąg dalszy...")
