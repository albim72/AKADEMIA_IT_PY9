class Kolor:

    # definicja stanu - konstruktor klasy
    def __init__(self, id_, nazwa):
        self.idkoloru = id_
        self.nazwa = nazwa
        self.paleta = "Paleta X"
        __ukryty = "5555"
        self.__info()


    # definicja zachowania -> funkcje klasy /metody/
    def print_kolor(self):
        print(f"id koloru: {self.idkoloru}, nazwa koloru: {self.nazwa}, paleta: {self.paleta}")

    def __info(self):
        print("to jest metoda z __")


k1 = Kolor(23, "niebieski")
k2 = Kolor(14, "czerwony")

k1.print_kolor()
k2.print_kolor()

k3 = Kolor(1, "biały")
k3.paleta = "Paleta 0"
#k3.__ukryty = "6543"

k3.print_kolor()
#print(k3.__ukryty)

k1.print_kolor()
#print(k1.__ukryty)
