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
