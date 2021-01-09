plik = open('dane/slowa.txt', 'r')
suma = 0
linie = plik.readlines()
for linia in linie:
    liczba = linia.strip()
    czy_jeden = False
    ok = True
    if liczba[0] != '0':
        ok = False
    for i in range(0,len(liczba)):
        if liczba[i] == '1' and not czy_jeden:
            czy_jeden = True
        if liczba[i] == '0' and czy_jeden:
            ok = False
    if not czy_jeden:
        ok = False
    if ok:
        suma = suma + 1
print(str(suma))