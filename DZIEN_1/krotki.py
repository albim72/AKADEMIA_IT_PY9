#tuple - krotka
animal = ("pies","kot","papuga","koń","krowa","skunks","pies")
print(animal)

#czy istenieją fukcje dla krotki: dodawanie,usuwanie,sortowanie,szukanie ndeksu, szukanie powtórzeń????
ip = animal.index("pies")
print(ip)
print(animal.count("pies"))

#del animal[ip]

print(animal[2:5])

for a in animal:
    print(a)

if "papuga" in animal:
    print("Tak! Papuga to zwierz")

if "budynek" in animal:
    print("Bład!")

anim2 = ("pająk","ryba")
animal = animal + anim2

print(animal)

takiedane = ("obiekt33",33,10.055,"Toruń",8,777.0001,True)
mojakrotka = tuple(takiedane)
print(mojakrotka)
print(type(mojakrotka))

#dokonaj w krotce następujących zmian:
#usuń wartość 10.055
#zamień wartość "Toruń" na "Gdańsk"
#dodaj na końcu wartość 1000

mojalista = list(mojakrotka)
print(mojalista)
mojalista.remove(10.055)
it = mojalista.index("Toruń")
mojalista[it] = "Gdańsk"
mojalista.append(1000)

mojakrotka = tuple(mojalista)
print(mojakrotka)

samochod = ('audi','Q7',2018,4.6)
print("rocznik",samochod[2])

(marka,model,rocznik,poj) = samochod

print("marka",marka)
print("model",model)
print("rocznik",rocznik)
print("pojemnosć",poj)



