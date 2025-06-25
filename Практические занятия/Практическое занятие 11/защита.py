#Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
import random
matrix = [[random.randint(1,10) for i in range(3)] for i in range(3)]

for i in matrix:
    print(' '.join(map(str, i)))

izm = [matrix[i] for i in range(len(matrix)) if i % 2 == 0]

filt = list(map(lambda i: sum(i) / len(i) if len(i) > 0 else 0, izm))

print(filt)
print(izm)