#Организовать словарь на 10 англо-русских слов, обеспечивающий "перевод" английского слова на русский
russ_eng = {"football": "футбол", "basketball": "баскетбол", "hockey": 'хоккей'
            , "volleyball": "воллейбол", "biathlon": "биатлон", "computer": "компьютер"
            , "joystick": "джостик", 'printer': 'принтер', 'laser': 'лазер', 'telephone': 'телефон'}
trans = input("Введите слово на английском с маленькой буквы: ")
print(russ_eng.get(trans))