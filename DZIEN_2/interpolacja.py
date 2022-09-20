miasto = "Lublin"
wiek = 34
imie = "Olga"

dane = "dane klienta - > imię: {}, miasto: {}, wiek: {}."
print(dane.format(imie,miasto,wiek))

dane = "dane klienta - > imię: {0}, wiek: {2}, miasto: {1}."
print(dane.format(imie,miasto,wiek))

wydzial = "Fizyki, Matematyki i Infromatyki"
uczelnia = "UMCS"
#f-string
student = f"Student - > Uczelnia: {uczelnia}, wydział: {wydzial}, imię: {imie},wiek: {wiek},miasto: {miasto}"

print(student)

identyfikator = "abc01"
wart = 6.4321678

formatowanie = '%-30s = %.2f' %(identyfikator,wart)
print(formatowanie)

print(f"wartość: {wart:.2f}")

owoce = [
    ('awokado',8.99),
    ('borówka amerykańska',21.22),
    ('banan',4.99),
    ('mandarynka',8.81),
    ('arbuz',3.69),
    ('jabłko',2.55),
    ('malina',120.52)
]

#sprządż cennik warzywniakawg wzoru: #nr nazwa(min dl. 10 znaków) = cena zł
#nr pozycji pobierz jako indeks listy owoce

en = list(enumerate(owoce))
print(en)
print("_________CENNIK WARZYWNIAKA__________")
for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-10s = %.2f zł' %(i,nazwa,cena))

print("_________NOWY CENNIK WARZYWNIAKA__________")
for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-20s = %6.2f zł' %(
        i+1,
        nazwa.title(),
        round(cena,1)
    ))
