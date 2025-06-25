#В двумерном списке элементы последней строки заменить на 0
import random

spis = [[random.randint(1, 10) for i in range(3)] for i in range(3)]
s = len(spis) - 1
new_spis = map(lambda i: [0]*len(i) if spis.index(i) == len(spis)-1 else(i), spis)

print('Вот изначальный список: ')

for i in spis:
    print(' '.join(map(str, i)))
print('Вот список с замененной последней строкой: ')

for i in new_spis:
    print(' '.join(map(str, i)))