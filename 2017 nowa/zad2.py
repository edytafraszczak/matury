file = open('dane.txt', 'r')
ile_u = 0
for linia in file.readlines():
    piksele = linia.strip().split(' ')
    ma_os = True
    for i in range(0,len(piksele)):
        p1 = int(piksele[i])
        p2 = int(piksele[-1-i])  
        if p1 != p2:
            ma_os = False
    if ma_os:
        ile_u+=1


print(' ile_u = {}'.format(ile_u))