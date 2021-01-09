def bin_to_int(liczba):
    suma = 0
    for i in range(0,len(liczba)):
        if liczba[i] == '1':
            suma = suma + pow(2,len(liczba)-1-i)
    return suma

def int_to_bin(liczba):
    liczba_do_dz = liczba
    wynik = ''
    while liczba_do_dz != 0:
        reszta = liczba_do_dz%2
        liczba_do_dz =(int)( liczba_do_dz/2)
        wynik = str(reszta) + wynik
    return wynik


plik = open('dane/binarne.txt', 'r')
najw = 0
linie = plik.readlines()
for linia in linie:
    liczba = linia.strip()
    # l_dz = int(liczba, 2)
    l_dz = bin_to_int(liczba)
    if l_dz < 65535:
        if l_dz > najw:
            najw = l_dz

print('suma to ' + str(najw) + ' ' + str(int_to_bin(najw)))