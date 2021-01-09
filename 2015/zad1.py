file = open('liczby.txt', 'r')
p2 = 0
p8 = 0
for linia in file.readlines():
    liczba = int(linia.strip(),2)
    if liczba%2 == 0:
        p2+=1
    if liczba%8 == 0:
        p8+=1
print('p2 = {} p8 = {}'.format(p2,p8))