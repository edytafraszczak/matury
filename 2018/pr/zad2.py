plik = open('dane/slowa.txt', 'r')
suma = 0
linie = plik.readlines()
for linia in linie:
    slowa = linia.strip().split(' ')
    if slowa[0] in slowa[1]:
        suma = suma + 1

print('suma =' + str(suma))