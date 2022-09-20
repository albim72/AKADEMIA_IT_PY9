#funckja nr 1

def witaj():
    print("witaj nowy użytkowniku")
    print("opłać abonament")
    print("zaloguj się....")

witaj()
witaj()

# for _ in range(1,35,2):
#     witaj()


for i in range(1,35,2):
    print("wykonanie funckji witaj nr:",i+1)
    witaj()


#funckja nr 2

def obywatel(paszport,kraj="Polska"):
    print("Kraj pochodzenia:",kraj,", paszport -> ", paszport)

obywatel("RT45435534","Norwegia")
obywatel("RF45435534","Niemcy")
obywatel("DD45435534","Szkocja")
obywatel("XC45435534",["Turcja","Mołdawia"])
obywatel("IO45435534")
obywatel("Anglia")
obywatel(kraj="Włochy",paszport="YUUI4456")
obywatel(paszport="YUUI4456erewr")

#funckja nr 3

def fx(n):
    return n**4

f = 100
def obliczenie(a,b,x):
    global f
    nb = fx(b)
    f = (a+b)*x + f + nb
    return f

print(obliczenie(4,2,3))
print(f)

#funckja nr 4

def miasta(miasto3,miasto2="Lublin",miasto1="Kraków",dodatkowe="Opole"):
    print("miasto tygodnia:",miasto1,", drugie miejsce:",miasto2,", trzecie miejsce:",miasto3)

miasta("Rzeszów","Toruń","Zamość")
miasta("Katowice","Kielce")
miasta("Gliwice")
miasta("Gliwice",None,"Gdańsk")
miasta("Gliwice",miasto1="Gdańsk",dodatkowe="Ustka")
miasta("Gliwice",dodatkowe="Ustka")
miasta(miasto3="Gliwice",dodatkowe="Ustka")

#funckja nr 5

def zamki(id,*zamek,rabat):
    print("zamek tygodnia:",zamek[0],"id:",id,"->rabat:",rabat,"zł, drugie miejsce:",zamek[1],", trzecie miejsce:",zamek[2])

zamki(1,"Malbork","Czersk","Będzin",rabat=20)
zamki(2,"Janowiec","Malbork","Chojnik","Czersk","Będzin","Kętrzyn",rabat=5)

a = 45
b = 12

assert a is not b
