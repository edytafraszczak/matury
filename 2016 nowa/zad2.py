file = open('dane_6_2.txt', 'r')
file1 = open('wyniki_6_2.txt', 'w')
k = 0
wynik = []
for linia in file.readlines():
    linia = linia.strip()
    if len(linia.split(' ')) != 2:
        continue
    k = int(linia.split(' ')[1])
    slowo = linia.split(' ')[0]
    wynik_linia = ''
    for znak in slowo:
        znak_ascii = ord(znak)
        znak_ascii = znak_ascii - k % 26
        if znak_ascii < 65:
            roznica = 65 - znak_ascii - 1
            znak_ascii = 90 - roznica
        znak = chr(znak_ascii)
        wynik_linia+=znak
    wynik.append(wynik_linia + '\n')
file1.writelines(wynik)