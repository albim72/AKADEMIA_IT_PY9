class Osoba:

    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczy = "brązowy"
        self.info()

    def info(self):
        print("Tworzenie nowej osoby na podstawie klasy Osoba...")

    def print_osoba(self) -> None:
        print(f"osoba -> imię: {self.imie}, wiek: {self.wiek}, wzrost: {self.wzrost} cm,"
              f" waga: {self.waga} kg, kolor oczu: {self.kolor_oczy}")

    def wiekza10lat(self) -> int:
        return  self.wiek +10

    def czypracownik(self) -> bool:
        return False

os1 = Osoba("Jan",45,102,173)
os1.print_osoba()
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os1.czypracownik()})")

print("_________________________________________________")

os2 = Osoba("Anna",32,56,166)
os2.kolor_oczy = "niebieskie"
os2.print_osoba()
print(f"wiek za 10 lat: {os2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os2.czypracownik()})")


class Pracownik(Osoba):

    #konstruktor z dziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,wiek,waga,wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self) -> None:
        print(f"dane pracownika -> firma: {self.firma}, stanowisko: {self.stanowisko}, lata pracy: "
              f"{self.latapracy}, wynagrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self) -> bool:
        return True

print("__________________________________________________")

pr1 = Pracownik("Adam",34,87,180,"ABC","dyrektor",8,9800)
pr1.print_osoba()
pr1.print_pracownik()
print(f"wiek za 10 lat: {pr1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({pr1.czypracownik()})")

class Sport:
    
    def __init__(self,dyscyplina,lata_upr,best_wynik):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.best_wynik = best_wynik
        
    def inforsport(self):
        print(f"dysycyplina: {self.dyscyplina}, lata uprawiania: {self.lata_upr}, życiówka: {self.best_wynik}")
        
class Ekstra:
    pass

class Student(Pracownik,Sport,Ekstra):
    
    #konstruktor z dziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,nr_studenta,wydzial,kierunek,rok_stud,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lata_upr="",best_wynik=""):
        Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
        self.nr_studenta = nr_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rok_stud = rok_stud

     def print_student(self) -> None:
        print(f"dane studenta nr  {self.nr_studenta}, wydział: {self.wydzial}, kierunek: {self.kierunek}, "
              f"rok studiów: {self.rok_stud}")

    def czypracownik(self) -> bool:
        return self.firma != ""

    print("_______________________________________________")

st1 = Student("Olaf",22,80,174,34534,"Budowlany","konstrukcja mostów",3)
st1.print_osoba()
st1.print_student()
print(f"wiek za 10 lat: {st1.wiekza10lat()}")
print(f"czy student jest pracownikiem? ({st1.czypracownik()})")

print("_______________________________________________")

st2 = Student("Olga",23,60,172,5353455,"Matematyki i Informatyki","Informatyka",4,
              "XYZ","młodszy programista",1,3000)
st2.print_osoba()
st2.print_student()
st2.print_pracownik()
print(f"wiek za 10 lat: {st2.wiekza10lat()}")
print(f"czy student jest pracownikiem? ({st2.czypracownik()})")

print("_______________________________________________")

st3 = Student("Robert",22,78,177,4354345,"Nauk Społecznych","Socjologia",3,
              dyscyplina="ultra biegi",lata_upr=5,best_wynik="102km 18h 45min 5s")
st3.print_osoba()
st3.print_student()
st3.inforsport()
print(f"wiek za 10 lat: {st3.wiekza10lat()}")
print(f"czy student jest pracownikiem? ({st3.czypracownik()})")
