file = open('dane.txt', 'r')
min = 8379834793
max = -8384303
for linia in file.readlines():
    for piksel in linia.strip().split(' '):
        piksel_l = int(piksel)
        if piksel_l < min:
            min = piksel_l
        if piksel_l > max:
            max = piksel_l
print(' min = {} max = {}'.format(min,max))