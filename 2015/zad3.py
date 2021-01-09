file = open('liczby.txt', 'r')
min = 208497
max = -738648
min_wiersz = 0
max_wiersz = -1
index = 1

for linia in file.readlines():
    liczba = int(linia.strip(), 2)
    if liczba > max:
        max = liczba
        max_wiersz = index
    if liczba < min:
        min = liczba
        min_wiersz = index
    index+=1
print('min = {} max = {}'.format(min_wiersz,max_wiersz))