#Организовать и вывести последовательность из 20 целых чисел, выбрать не
#повторяющиеся элементы, найти их количество. Элементы больше 5 увеличить в два раза.
import random
from functools import reduce

posl = [random.randint(1,20) for x in range(20)]
print("Исходная последовательность:", " ".join(map(str, posl)))

unik = set(posl)
print("Уникальные элементы:", ' '.join(map(str, unik)))

print(f'Количество уникальных элементов: {len(unik)}')

newspis = list(map(lambda x: x * 2 if x > 5 else x, unik))
print("Модифицированные уникальные элементы:", " ".join(map(str, newspis)))