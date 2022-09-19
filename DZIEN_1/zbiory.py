drzewa = {'buk','jodła','dąb','jesion','baobab','jabłoń','sosna'}
print(drzewa)
print(drzewa)
print(drzewa)

print("_____________________________________")
for d in drzewa:
    print(d)
j = "jesion" in drzewa
print(j)
print("osika" in drzewa)

drzewa.add("osika")
print(drzewa)

ekstra = ["topola","wierzba","świerk","śliwa","świerk"]
drzewa.update(ekstra)
print(drzewa)

se = set(ekstra)
print(se)

drzewa.remove("śliwa")
print(drzewa)

drzewa.discard("jojoba")
print(drzewa)

drzewa.discard("dąb")
print(drzewa)


nowedrzewa = frozenset(ekstra)
print(nowedrzewa)

nd = set(nowedrzewa)
