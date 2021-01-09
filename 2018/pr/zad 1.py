plik = open('dane/slowa.txt', 'r')
suma = 0
linie = plik.readlines()
for linia in linie:
    slowa = linia.strip().split(' ')
    if slowa[0].endswith('A'):
        suma = suma + 1
    if slowa[1].endswith('A'):
        suma = suma + 1
print('suma =' + str(suma))