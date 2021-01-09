def szyfruj(slowo,k):
    wynik_linia = ''
    for znak in slowo:
        znak_ascii = ord(znak)
        znak_ascii = znak_ascii - k % 26
        if znak_ascii < 65:
            roznica = 65 - znak_ascii - 1
            znak_ascii = 90 - roznica
        znak = chr(znak_ascii)
        wynik_linia+=znak
    return wynik_linia

file = open('dane_6_3.txt', 'r')
file1 = open('wyniki_6_3.txt', 'w')
wynik = []
for linia in file.readlines():
    linia = linia.strip()
    if len(linia.split(' ')) != 2:
        continue
    slowo = linia.split(' ')[0]
    slowo2 = linia.split(' ')[1]
    pop = False
    for k in range(0,26):
        szyfr = szyfruj(slowo,k)
        if slowo2 == szyfr:
            pop = True
    if pop == False:
        wynik.append(slowo + ' ' + slowo2 + '\n')

file1.writelines(wynik)