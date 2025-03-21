# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах
# можно приобрести книги Пушкина и Тютчева
    
magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
homebook = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bookshop = {'Пушкин', 'Достоевский', 'Маяковский'}
galary = {'Чехов', 'Тютчев', 'Пушкин'}

pushityt = {"Тютчев","Пушкин"}
shop = {}
shop = set(shop)
if (pushityt & magistr) == pushityt:
    shop.add("Магистр")
if (pushityt & homebook) == pushityt:
    shop.add("ДомКниги")
if (pushityt & bookshop) == pushityt:
    shop.add("БукМаркет")
if (pushityt & galary) == pushityt:
    shop.add("Галерея")

print("Книги Пушкина и Тютчева есть в", ", ".join(shop))
