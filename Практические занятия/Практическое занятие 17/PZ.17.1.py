import tkinter as tk
from datetime import datetime

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("400x600")
        self.root.configure(bg='#333366')  # Темно-синий фон
        
        # Основные цвета
        self.bg_color = '#333366'
        self.entry_bg = '#dddddd'
        self.button_bg = '#FF8C00'  # Оранжевый
        self.text_color = '#ffffff'
        
        self.create_widgets()
    
    def create_widgets(self):
        # Заголовок
        tk.Label(
            self.root, 
            text="Sign Up", 
            font=('Arial', 16, 'bold'),
            bg=self.bg_color,
            fg='yellow'
        ).pack(pady=10)
        
        # Фрейм для полей ввода
        form_frame = tk.Frame(self.root, bg=self.bg_color)
        form_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Поля формы
        fields = [
            ("First Name", "Enter First Name..."),
            ("Last Name", "Enter Last Name..."),
            ("Screen Name", "Enter Screen Name..."),
            ("Date of Birth", ""),
            ("Gender", ""),
            ("Country", ""),
            ("E-mail", "Enter E-mail......"),
            ("Phone", "Enter Phone......"),
            ("Password", ""),
            ("Confirm Password", "")
        ]
        
        self.entries = {}
        for i, (label, placeholder) in enumerate(fields):
            tk.Label(
                form_frame, 
                text=label, 
                bg=self.bg_color, 
                fg=self.text_color,
                anchor='w'
            ).grid(row=i, column=0, sticky='ew', pady=5)
            
            if label == "Date of Birth":
                # Поле для даты рождения
                dob_frame = tk.Frame(form_frame, bg=self.bg_color)
                dob_frame.grid(row=i, column=1, sticky='ew')
                
                self.month_var = tk.StringVar(value='May')
                months = ['January', 'February', 'March', 'April', 'May', 'June', 
                         'July', 'August', 'September', 'October', 'November', 'December']
                tk.OptionMenu(dob_frame, self.month_var, *months).pack(side=tk.LEFT)
                
                self.day_var = tk.StringVar(value='5')
                tk.Spinbox(dob_frame, from_=1, to=31, textvariable=self.day_var, width=3).pack(side=tk.LEFT, padx=5)
                
                current_year = datetime.now().year
                self.year_var = tk.StringVar(value='1985')
                tk.Spinbox(dob_frame, from_=1900, to=current_year, textvariable=self.year_var, width=5).pack(side=tk.LEFT)
                
            elif label == "Gender":
                # Радиокнопки для пола
                gender_frame = tk.Frame(form_frame, bg=self.bg_color)
                gender_frame.grid(row=i, column=1, sticky='w')
                
                self.gender_var = tk.StringVar(value='Male')
                tk.Radiobutton(
                    gender_frame, text="Male", variable=self.gender_var, value="Male",
                    bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color
                ).pack(side=tk.LEFT)
                tk.Radiobutton(
                    gender_frame, text="Female", variable=self.gender_var, value="Female",
                    bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color
                ).pack(side=tk.LEFT, padx=10)
                
            elif label == "Country":
                # Выпадающий список для страны
                self.country_var = tk.StringVar(value='USA')
                countries = ['USA', 'Canada', 'UK', 'Russia', 'Germany', 'France']
                tk.OptionMenu(
                    form_frame, self.country_var, *countries
                ).grid(row=i, column=1, sticky='ew')
                
            else:
                # Обычные поля ввода
                entry = tk.Entry(
                    form_frame, 
                    bg=self.entry_bg,
                    fg='black',
                    insertbackground='black'
                )
                entry.insert(0, placeholder)
                if "Password" in label:
                    entry.config(show="*")
                entry.grid(row=i, column=1, sticky='ew', pady=5)
                self.entries[label] = entry
        
        # Чекбокс "Terms of Use"
        self.terms_var = tk.BooleanVar()
        tk.Checkbutton(
            form_frame, 
            text="I agree to the Terms of Use",
            variable=self.terms_var,
            bg=self.bg_color,
            fg=self.text_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.text_color
        ).grid(row=len(fields), column=0, columnspan=2, pady=20, sticky='w')
        
        # Плашка с кнопками (оранжевая)
        button_frame = tk.Frame(self.root, bg=self.button_bg)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=0, pady=0)
        
        # Кнопки
        tk.Button(
            button_frame,
            text="Submit",
            bg='green',
            fg='white',
            padx=20,
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT
        ).pack(side=tk.LEFT, padx=20, pady=10)
        
        tk.Button(
            button_frame,
            text="Cancel",
            command=self.root.destroy,
            bg='red',
            fg='white',
            padx=20,
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT
        ).pack(side=tk.RIGHT, padx=20, pady=10)
        
        # Настройка отступов
        form_frame.columnconfigure(1, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()