def dziel(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("dzielenie przez 0!")
    except NameError:
        print("brak danych")
    except TypeError:
        print("dziel tylko wartości liczbowe!")
    except:
        print("coś poszło nie tak....")
    else:
        print(f"wynik dzielenia: {wynik}")
    finally:
        print("policzmy coś jeszcze.....")


try:
    dziel(1,1)
    dziel(1,0)
    dziel(0,0)
    dziel(0.555,-9.99)
    dziel(3,True)
    dziel(33,False)
    dziel("afaas",False)
    dziel(31)
except TypeError:
    print("niewłaściwa liczba argumentów funkcji")
