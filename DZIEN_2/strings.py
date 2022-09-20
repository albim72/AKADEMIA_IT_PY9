mecz = "MECZ MIESIĄCA:\nKlub sportowy: \"Orły Wisła\" - \tTrener: Jan Kot\nlokalizacja klubu: Janowo\n" \
       "vs\nKlub sportowy: \"KS Leśnik\" - \tTrener: Adam Nowak\nlokalizacja klubu: Leśne Ostępy\n"

print(mecz)

str_ = "         niezwykle ważna i Tajna wiadomość;    RT63745867368;   i Tajna PrzeSyłKA"
print(str_.lower())
print(str_.upper())
print(str_.strip())
print(str_.replace("Tajna","Utajniona"))
frag = str_.split(";")
print(frag[1])

for i,fr in enumerate(frag):
    frag[i] = frag[i].strip()

print(frag)

print(str_.find("Tajna"))
print(str_.endswith("ka"))
print(str_.endswith("KA"))

d = "pionierzy"
e = "1002"

print(d.isalpha())
print(e.isdigit())
