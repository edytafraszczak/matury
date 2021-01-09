fh = open('dane/dzialki.txt', 'r')
linie = fh.readlines()
liczba_t = 0
liczba_z = 0
liczba_d = 0
for linia in linie:
    if linia == '\n':
        procent = liczba_t * 1.0 / liczba_z
        if procent >= 0.7:
            liczba_d = liczba_d + 1
        liczba_t = 0
        liczba_z = 0
    else:
        for znak in linia:
            if znak != '\n':
                if znak == '*':
                    liczba_t = liczba_t + 1
                liczba_z = liczba_z + 1

print('liczba_d ' + str(liczba_d))
