class Miasto:

    def __init__(self,id,nazwa,woj):
        self.id = id
        self.nazwa = nazwa
        self.woj = woj

    def print_miasto(self):
        print(f"miasto: {self.nazwa}, województwo: {self.woj}")
