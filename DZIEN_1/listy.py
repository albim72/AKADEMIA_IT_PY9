kraje = ['Polska','Szwecja','Hiszpania','Niemcy','Włochy']
print(kraje)
print(kraje[2])
print(kraje[1:4])
print(kraje[3:])
kraje.append('Szwecja')
print(kraje)
print(kraje.index("Szwecja"))
print(kraje.count("Szwecja"))
kraje[2] = "Szwecja"
print(kraje)
kraje.insert(3,"Polska")
print(kraje)

kraje[2],kraje[3] = kraje[3],kraje[2]

print(kraje)
kraje[2],kraje[6] = kraje[6],kraje[2]

print(kraje)
kraje[0],kraje[1],kraje[2] = kraje[1],kraje[0],kraje[2]

print(kraje)

kraje.sort()
print(kraje)

kraje.reverse()
print(kraje)

kraje.sort(reverse=True)
print(kraje)

liczby = [2,67,88,92,14,69,112,0,112,0,34,67,112,17,55,-10]

liczby.sort()
print(liczby)

liczby.remove(112)
print(liczby)

si = liczby.index(67)
del liczby[si]

print(liczby)

liczby[2:7] = ["takie","tam","coś"]

print(liczby)

stan = [[4,2,2],3,1,12,3,1]
rasy=['buldog angielski','rodezjan','owczarek podhalański']
sklepzoo = [[rasy,"kot","papuga","mysz","szynszyla","słoń"],[[7200,6700,5500],2400,8900,34,250],stan]

print(sklepzoo[0][0][0],"-",sklepzoo[1][0][0],"zł, na stanie - ",sklepzoo[2][0][0])
print(sklepzoo[0][5],"-","brak","zł")

print(sklepzoo)

miasto = ['Toruń','Katowice','Lublin']
stolica = ['Warszawa']

miasto = miasto + stolica
print(miasto)

miasto = miasto + ['Koszalin','Zamość']
print(miasto)
miasto = miasto*3
print(miasto)

litery = ['a','b','c','d','e','f','g','h']

print("litery przez zmianą:",litery)

litery[2:7] = [99,23,56]
print("litery po zmianie:",litery)

litery_m = litery
litery_p = list(litery)
litery_q = litery[:] #nowa instancja listy litery (nowy adres pamięci)

print("litery przez zmianą:",litery)
print("litery_m przez zmianą:",litery_m)
print("litery_p przez zmianą:",litery_p)
print("litery_q przez zmianą:",litery_q)

litery[:] = [1001,1002,1455,1988]

print("litery po zmianie:",litery)
print("litery_m po zmianie:",litery_m)
print("litery_p po zmianie:",litery_p)
print("litery_q po zmianie:",litery_q)

kolory = ['czerwony','biały','czarny','fioletowy','niebieski','zielony']
#stwórz listy parz i nieparz
#w liście parz ulokuj wszyskie elementy listy kolory z pozycji parzystch
#w liście nieparz ulokuj wszyskie elementy listy kolory z pozycji nieparzystch

parz = kolory[::2]
nieparz = kolory[1::2]


print(parz)
print(nieparz)

nb = [4,3,3,6,8,90,23,12,6,9,11,14,6]
newtab = nb[2:6:2]
print(newtab)

w1 = "kajak"
w2 = "pomarańcza"

#odwróć wyrazy -> wypisz je odwrotnie(od prawej do lewej)

ws1 = w1[::-1]
ws2 = w2[::-1]

print(w1,ws1)
print(w2,ws2)
