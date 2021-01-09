def dziala(mapa):
    max_rozmiar = 0
    for i in range(30):



def wypisz(mapa, odwr=False):
    if odwr:
        f = open("dane/dzialki_odw.txt", "a")
    else:
        f = open("dane/dzialki_www.txt", "a")

    for index in range(0, len(mapa)):
        if odwr:
            f.write(mapa[index][::-1])
        else:
            f.write(mapa[index])
    f.close()


def czy_mapy_rowne(mapa, mapa_do_odwr):
    for index in range(0, len(mapa)):

        linia_odwr = mapa_do_odwr[index][::-1]
        linia = mapa[index]
        for index_znaku in range(0, len(linia)):
            try:
                if not linia[index] or not linia_odwr[index]:
                    continue
                if linia[index] != linia_odwr[index]:
                    return False
            except:
                print(linia + ' ' + str(index) + ' ' + linia_odwr)
    return True


fh = open('dane/dzialki_1.txt', 'r')
linie = fh.readlines()
linie_odwrocone = linie

for i in range(0, len(linie), 31):
    mapa = linie[i:i + 31]
    mapa_odw = list(reversed(linie_odwrocone[i:i + 31]))
    if czy_mapy_rowne(mapa, mapa_odw):
        print(str(i) + ' mapy sa identyczne')
    wypisz(mapa)
    wypisz(mapa_odw, True)
