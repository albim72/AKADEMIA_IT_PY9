from miasto import Miasto

class Stolica(Miasto):

    def __init__(self,id, nazwa, woj, prezydent):
        super().__init__(id, nazwa, woj)
        self.prezydent = prezydent

    def prezydent_info(self):
        print(f"prezydent stolicy: {self.prezydent}")
