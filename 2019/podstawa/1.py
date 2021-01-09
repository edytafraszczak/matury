fh = open('dane/dane.txt', 'r')
linie = fh.readlines()
liczba_m = 0
liczba_k = 0
for linia in linie:
    liczba = int(linia[9])
    if liczba % 2 == 0:
        liczba_k = liczba_k + 1
    else:
        liczba_m = liczba_m + 1

print('liczba_k ' + str(liczba_k))
print('liczba_m ' + str(liczba_m))
