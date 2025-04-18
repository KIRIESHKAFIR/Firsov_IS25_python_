# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Среднее арифметическое элементов первого и второго файлов:
# Количество нечетных элементов первого и второго файлов:
# Элементы общие для двух файлов:
# Количество элементов, общих для двух файлов

g = [x for x in range(int(input("Введите начало 1 послед: ")),int(input("Введите конец 1 послед: "))+1)]
f = [x for x in range(int(input("Введите начало 2 послед: ")),int(input("Введите конец 2 послед: "))+1)]

file1 =  open('чет.txt', "w", encoding="utf-8")
file1.write(" ".join(map(str,g)))

file2 = open('нечет.txt', "w", encoding="utf-8")
file2.write(" ".join(map(str,f)))

file3 = open('new.txt', "w", encoding='utf-8')

fg = (sum(g)+sum(f)) / (len(g)+len(f))
print(fg, sum(g))

def nchEl(nch_count , _list):
    for i in _list:
        if i % 2 != 0:
            nch_count += 1
    return nch_count

def ob(list1, list2):
    count = 0
    el_list = []
    for i in list1:
        if i in list2:
            el_list.append(i)
            count += 1
    return el_list, count
            
nch = 0
nch = nchEl(nch,g)
nch = nchEl(nch,f)

els_list, count_of_el = ob(g,f)
print(nch)
print( els_list )
print(count_of_el)
file3.write(f"{', '.join(map(str,g))}, {', '.join(map(str,f))} - элементы двух списков\n")
file3.write(f'{fg} - среднее арифметическое\n')
file3.write(f"{nch} - количество нечетных эл-тов\n")
file3.write(f"{', '.join(map(str,els_list))} - одинаковые элементы\n")
file3.write(f'{count_of_el} количество одинаковых элементов\n')