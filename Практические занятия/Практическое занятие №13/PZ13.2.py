#В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два раза
import random

spis = [[random.randint(1, 10) for i in range(5)] for i in range(5)]
N = int(input("Введите номер столбца, который будет умножена на 2: ")) - 1

new_spis =map(lambda i: i[:N] + [i[N]*2] + i[N+1:] if N < len(i) else i, spis)

print("Вот старый двумерный список: ")

for i in spis:
    print(' '.join(list(map(str, i))))
    
print("Вот новый двумерный список: ")
for i in new_spis:
    print(' '.join(list(map(str, i))))