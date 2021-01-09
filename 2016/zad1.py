plik = open('dane/slowa.txt', 'r')
suma = 0
linie = plik.readlines()
for linia in linie:
    liczba = linia.strip()
    zero = 0
    for i in range(0,len(liczba)):
        if liczba[i] == '0':
            zero = zero + 1
    if zero > len(liczba)/2:
        suma = suma  + 1

print(str(suma))
