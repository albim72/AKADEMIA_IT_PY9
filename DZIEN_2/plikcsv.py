import csv

with open("firma.csv",encoding="utf-8") as pc:
    csv_reader = csv.reader(pc,delimiter=";")
    licznik_linii = 0
    for wiersz in csv_reader:
        if licznik_linii == 0:
            print(f'Nazwa kolumny: {", ".join(wiersz)}')
            licznik_linii += 1
        else:
            print(f'\t{wiersz[0]} pracuje na stanowisku: {wiersz[1]} i ma urodziny w miesiącu: {wiersz[2]}'
                  f', otrzymuje nagrodę pienieżną w wysokości: {wiersz[3]} zł')
            licznik_linii += 1
    print(f'wczytano {licznik_linii} linii')
    print(f'wczytano {licznik_linii-1} pracowników')
