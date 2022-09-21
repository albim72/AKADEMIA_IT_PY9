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
              f" waga: {self.waga} kg")

    def wiekza10lat(self) -> int:
        return  self.wiek +10

    def czypracownik(self) -> bool:
        return False
