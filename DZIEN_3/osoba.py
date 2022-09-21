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

