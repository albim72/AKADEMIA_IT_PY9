#słownik(dictionary) -> klasa: dict, struktura asocjacyjna (klucz,wartość)
#klucz(number, str) - sposób na indeksację elementów

samochod = {
    "marka":"Ford",
    "model":"Mustang",
    "rocznik":1973
}

print(samochod)
print(samochod["model"])
print(samochod.get("model"))
samochod["rocznik"] = 2018

print(samochod)
samochod["poj"] = 4.5

print(samochod)

# samochod["marka"],samochod["model"] = samochod["model"],samochod["marka"]
# print(samochod)

print(samochod.items())
print(samochod.keys())
print(samochod.values())

print("_____klucze_____")
for x in samochod:
    print(x)

print("_____wartości_____")

for y in samochod.values():
    print(y)
print("_____wartości_____")

for y in samochod:
    print(samochod[y])

print("_______pary_________")

for x,y in samochod.items():
    print(x,":",y)


autokomis = {
    "auto1":{
        "marka":"Ford",
        "model":"Mustang",
        "rocznik":1973
    },
    "auto2":{
        "marka":"Opel",
        "model":"Insignia",
        "rocznik":2017
    },
    "auto3":{
        "marka":"Jeep",
        "model":"Cherokee",
        "rocznik":2020
    }
}

print(autokomis)
print(autokomis["auto2"])
print(autokomis["auto2"]["rocznik"])
