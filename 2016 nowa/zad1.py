file = open('dane_6_1.txt', 'r')
file1 = open('wyniki_6_1.txt', 'w')
k = 107
wynik = []
for linia in file.readlines():
    linia = linia.strip()
    wynik_linia = ''
    for znak in linia:
        znak_ascii = ord(znak)
        znak_ascii = znak_ascii + k % 26
        if znak_ascii > 90:
            znak_ascii = 65 + znak_ascii % 26
        znak = chr(znak_ascii)
        wynik_linia+=znak
    wynik.append(wynik_linia + '\n')
file1.writelines(wynik)