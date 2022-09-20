x = lambda a:a+331

print(x(45))

def policz(a):
    return a+331

print(policz(45))

y = lambda a,b,c=2:(a-b)*c

print(y(3,13.4,5))
print(y(3,13.4))

def multi(n):
    return lambda a:a*n

d = multi(56)
print(d(7))

print(multi(8)(19))

liczby = [34,2,1,-3,0,15,67,112,999,-100,34,57,9,11,45]
#stwórz listę parzyste do której wstwisz wszystkie wartości parzyte z listy liczby
parzyste = list(filter(lambda x:x%2==0,liczby)) #filter(funkcja_filtrująca,dane_lista)
#funkcja filtrująca przys spełnieniu warunku zwraca True i wtedy element listy jest podstawiany do nowej tablicy
print(parzyste)

def warunek(a,x):
    return a == 2*x
print(warunek(3,2))
print(warunek(6,3))

#stwórz listę cube do której wstawisz sześciany wartości z listy liczby

cube = list(map(lambda x:x**3,liczby))  #map(funkcja_mapująca,dane_lista)
print(cube)
