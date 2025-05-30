#В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
#ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
#текстовый файл все даты февраля в формате ДД/ММ/ГГГГ
import re

file = open('dates.txt', 'r', encoding='utf-8')
text = file.read()

toch = re.findall(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', text)
slash = re.findall(r'\b(\d{2})/(\d{2})/(\d{4})\b', text)

print(f"ДД.ММ.ГГГГ: {len(toch)}\nДД/ММ/ГГГГ: {len(slash)}")

fevral = [f"{d[0]}/{d[1]}/{d[2]}" for d in slash if d[1] == '02']

file = open('fevral.txt', 'w', encoding='utf-8')
file.write('\n'.join(map(str, fevral)))
file.close