#warunek

a = 1
b = 1

if a>b:
    print("a jest większe niż b")
elif a == 1 and b == 1:
    print("a=1 i b=1")
elif a == b:
    print("a jest równe b")
else:
    print("a jest miejsze niż b")

#tylko od wersji 10 Pythona
n=2
match n:
    case 1:print("jedynka")
    case 2:print("dwójka")
    case 3:print("trójka")


#iteracja

i=1
while i<=6:
    print(i)
    # if i==3:
    #     break

    #komentowanie wielu linii -> CTRL - /
    i+=2
else:
    print("faktycznie i =",i)

print("ciąg dalszy....")


owoce = ['jabłko','czereśnia','pomarańcza','kiwi','cytryna']
print(owoce)

for owoc in owoce:
    print(owoc)

print("___________________________________________")

cechy = ["kolorowy","elegancki","czysty","brudny","obskurny"]
obiekty = ["dom","samochód","płaszcz","ogórd","przystanek"]

for c in cechy:
    for o in obiekty:
        print(c,o)


#wyswietlenie co 2 elementu
for c in cechy[::2]:
    for o in obiekty:
        print(c,o)



