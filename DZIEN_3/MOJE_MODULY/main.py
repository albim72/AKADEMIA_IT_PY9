#import dane
#import dane as dn
from dane import osoba
from moje_funkcje import konferencja,policz
#from miasto import Miasto
from stolica import Stolica,Miasto
from ekstra.fx.policzmy import licz

print(osoba)
print(konferencja("Jan Kowal"))
print(f"wynik d = {policz(3,7)}")

ms = Miasto(2,"Kielce","świętokrzyskie")
ms.print_miasto()

st = Stolica(1,"Warszawa","mazowieckie","Jan Kot")
st.print_miasto()
st.prezydent_info()

print(f"wynik funkcji: {licz(45,7)}")
