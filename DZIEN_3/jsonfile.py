import json

json_str = '{"name":"Jan","age":67,"city":"Kraków"}'
print(json_str)
print(type(json_str))

dict_osoba = json.loads(json_str)
print(type(dict_osoba))
print(dict_osoba)
imie = dict_osoba["name"]
print(imie)

pojazd = {
    "marka":"Opel",
    "model":"Insignia",
    "rok":2019
}

print(type(pojazd))
jsonpojazd = json.dumps(pojazd,indent=4)
print(type(jsonpojazd))
print(jsonpojazd)

with open("pojazd.json","w",encoding="utf-8") as f:
    f.write(jsonpojazd)

with open("pojazd.json","r",encoding="utf-8") as f:
    p_dict = json.load(f)

print(p_dict)

