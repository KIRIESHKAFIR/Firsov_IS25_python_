import random
import tkinter as tk
from tkinter import ttk

def print_random_symbols():
    try:
        symbols_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя1234567890!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
        symbols = ''.join(random.choices(symbols_pool, k=40))
        result_label.config(text=f"Случайные символы: {symbols}")
        return symbols
    except Exception as e:
        result_label.config(text=f"Ошибка при генерации символов: {str(e)}")
        return ""

# Создаем главное окно
root = tk.Tk()
root.title("Генератор случайных символов")
root.geometry("600x200")
root.resizable(False, False)

# Устанавливаем тему
style = ttk.Style()
style.theme_use('clam')

# Создаем рамку для содержимого
frame = ttk.Frame(root, padding="20")
frame.pack(expand=True, fill='both')

# Заголовок
title_label = ttk.Label(frame, text="Генератор 40 случайных символов", font=('Helvetica', 14, 'bold'))
title_label.pack(pady=(0, 15))

# Кнопка генерации
generate_button = ttk.Button(frame, text="Сгенерировать символы", command=print_random_symbols)
generate_button.pack(pady=5)

# Поле для вывода результата
result_label = ttk.Label(frame, text="Здесь появятся сгенерированные символы...", 
                         wraplength=550, justify='center', font=('Helvetica', 11))
result_label.pack(pady=10, expand=True)

# Запускаем главный цикл
root.mainloop()