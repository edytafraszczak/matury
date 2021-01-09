plik = open('dane/binarne.txt', 'r')
suma = 0
najdluzszy = ''
linie = plik.readlines()
for linia in linie:
    liczba = linia.strip()
    najw_cykl = ''
    for i in range(1,(int) (len(liczba) / 2) +1):
        cykl = liczba[0:i]
        ok = True

        for j in range(0, len(liczba), len(cykl)):
            if cykl != liczba[j:len(cykl) + j]:
                ok = False
        if ok:
            najw_cykl = cykl
    if najw_cykl:
        suma = suma + 1
        if len(najdluzszy) < len(liczba):
            najdluzszy = liczba


print('suma =' + str(suma))
print('najdluzszy cykl to ' + najdluzszy + ' ' + str(len(najdluzszy)))
