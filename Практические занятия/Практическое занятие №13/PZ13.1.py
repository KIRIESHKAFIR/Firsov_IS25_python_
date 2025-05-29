#В двумерном списке элементы последней строки заменить на 0

spis = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
s = len(spis) - 1
for i in range(len(spis[s])):
    spis[s][i] = 0
print('Вот список с замененной последней строкой: ')
for i in spis:
    print(' '.join(map(str, i)))