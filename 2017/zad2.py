plik = open('dane/binarne.txt', 'r')
suma = 0
najkr = 'xdsssssffsdsdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
linie = plik.readlines()
for linia in linie:
    liczba = linia.strip()
    ok = True
    for i in range(0,len(liczba),4):
        l_dzies = liczba[i:i+4]
        if int(l_dzies,2) > 9:
            ok = False
    if not ok:
        suma = suma + 1
        if len(liczba) < len(najkr):
            najkr = liczba
print('suma to ' + str(suma) + ' '+ najkr)