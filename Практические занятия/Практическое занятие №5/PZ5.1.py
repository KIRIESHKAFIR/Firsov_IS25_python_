# Составить функцию, которая напечатает сорок любых символов.

import random
#Пишем функцию выполняющуюразные цифры
def print_random_symbols():
    try:
        symbols_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя1234567890!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
        symbols = ''.join(random.choices(symbols_pool, k=40))
        print("Случайные символы:", symbols)
        return symbols
    except Exception:
        print("Ошибка при генерации символов.")
        return ""

# Пример вызова
print_random_symbols()