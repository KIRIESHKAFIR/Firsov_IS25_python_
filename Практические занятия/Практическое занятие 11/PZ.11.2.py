#Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое,
#количество символов в тексте. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно вставив после строки N (N – задается пользователем)
#произвольную фразу
file = open('text18-28.txt','r',encoding='utf-16')
summary = file.readlines()
sum_str = "".join(summary)
print(sum_str)
print(f'\nКолличество символов: {len(sum_str)}')
print(f'\nКоличество символов: {len(summary)}')
fraz = input("Введите фразу: ")
n = int(input("Введите строку N: "))
summary.insert((n-1),(fraz+'\n'))
file2 = open('new_text18-28.txt','w',encoding='utf-8')
for line in summary:
    file2.write(line)
file.close()
file2.close()