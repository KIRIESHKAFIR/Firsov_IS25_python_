import tkinter as tk
from tkinter import ttk
from datetime import datetime

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("500x650")  # Увеличил ширину окна
        self.root.configure(bg='#000033')  # Сделал фон темнее
        self.setup_ui()
    
    def setup_ui(self):
        # Верхняя панель (оранжевая)
        top_frame = tk.Frame(self.root, bg='#FF8C00', height=50)
        top_frame.pack(fill=tk.X, side=tk.TOP)
        
        # Заголовок "Sign Up" (в оранжевой панели)
        tk.Label(
            top_frame,
            text="Sign Up",
            font=('Arial', 16, 'bold'),
            bg='#FF8C00',
            fg='yellow'
        ).pack(pady=10)

        # Основной фрейм (тёмно-синий)
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Стилизация
        style = ttk.Style()
        style.configure('TFrame', background='#000033')  # Более темный синий
        style.configure('TLabel', background='#000033', foreground='#FFFF00')
        style.configure('TEntry', fieldbackground='lightgray')
        style.configure('TRadiobutton', background='#000033', foreground='#FFFF00')
        
        # Поля формы
        fields = [
            ("First Name", "Enter First Name..."),
            ("Last Name", "Enter Last Name..."),
            ("Screen Name", "Enter Screen Name..."),
            ("E-mail", "Enter E-mail......"),
            ("Phone", "Enter Phone......"),
            ("Password", ""),
            ("Confirm Password", "")
        ]
        
        self.entries = {}
        for i, (label, placeholder) in enumerate(fields, start=1):
            ttk.Label(main_frame, text=label).grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(main_frame)
            entry.insert(0, placeholder)
            entry.grid(row=i, column=1, sticky=tk.EW, pady=5)
            self.entries[label] = entry
        
        # Дата рождения
        ttk.Label(main_frame, text="Date of Birth").grid(row=8, column=0, sticky=tk.W, pady=5)
        
        dob_frame = ttk.Frame(main_frame)
        dob_frame.grid(row=8, column=1, sticky=tk.EW)
        
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                 'July', 'August', 'September', 'October', 'November', 'December']
        self.month_var = tk.StringVar(value='May')
        ttk.Combobox(dob_frame, textvariable=self.month_var, values=months, width=10).pack(side=tk.LEFT)
        
        self.day_var = tk.StringVar(value='5')
        ttk.Spinbox(dob_frame, from_=1, to=31, textvariable=self.day_var, width=3).pack(side=tk.LEFT, padx=5)
        
        current_year = datetime.now().year
        self.year_var = tk.StringVar(value='1985')
        ttk.Spinbox(dob_frame, from_=1900, to=current_year, textvariable=self.year_var, width=5).pack(side=tk.LEFT)
        
        # Пол
        ttk.Label(main_frame, text="Gender").grid(row=9, column=0, sticky=tk.W, pady=5)
        gender_frame = ttk.Frame(main_frame)
        gender_frame.grid(row=9, column=1, sticky=tk.W)
        
        self.gender_var = tk.StringVar(value='Male')
        ttk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male").pack(side=tk.LEFT)
        ttk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female").pack(side=tk.LEFT, padx=10)
        
        # Страна
        ttk.Label(main_frame, text="Country").grid(row=10, column=0, sticky=tk.W, pady=5)
        self.country_var = tk.StringVar(value='USA')
        countries = ['USA', 'Canada', 'UK', 'Russia', 'Germany', 'France']
        ttk.Combobox(main_frame, textvariable=self.country_var, values=countries).grid(row=10, column=1, sticky=tk.EW)
        
        # Чекбокс "Terms of Use"
        self.terms_var = tk.BooleanVar()
        ttk.Checkbutton(
            main_frame,
            text="I agree to the Terms of Use",
            variable=self.terms_var
        ).grid(row=11, column=0, columnspan=2, pady=10)
        
        # Оранжевый фрейм для кнопок (во всю ширину)
        button_bg_frame = tk.Frame(main_frame, bg='#FF8C00', height=35)
        button_bg_frame.grid(row=12, column=0, columnspan=2, sticky='ew', pady=(20, 0))
        
        # Фрейм для кнопок (выравнивание по правому краю)
        button_frame = tk.Frame(button_bg_frame, bg='#FF8C00')
        button_frame.pack(side=tk.RIGHT, padx=20, pady=5)
        
        # Кнопки (сохраняем оригинальное форматирование)
        submit_btn = tk.Button(
            button_frame,
            text="Submit",
            command=self.submit,
            bg='green',
            fg='white',
            padx=20,
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT
        )
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        cancel_btn = tk.Button(
            button_frame,
            text="Cancel",
            command=self.root.destroy,
            bg='red',
            fg='white',
            padx=20,
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT
        )
        cancel_btn.pack(side=tk.LEFT)
        
        # Настройка веса колонок
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(12, weight=1)
    
    def submit(self):
        data = {
            'first_name': self.entries['First Name'].get(),
            'last_name': self.entries['Last Name'].get(),
            'screen_name': self.entries['Screen Name'].get(),
            'email': self.entries['E-mail'].get(),
            'phone': self.entries['Phone'].get(),
            'password': self.entries['Password'].get(),
            'confirm_password': self.entries['Confirm Password'].get(),
            'dob': f"{self.month_var.get()} {self.day_var.get()} {self.year_var.get()}",
            'gender': self.gender_var.get(),
            'country': self.country_var.get(),
            'terms_accepted': self.terms_var.get()
        }
        print("Registration data:", data)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()