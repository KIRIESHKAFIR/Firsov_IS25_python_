#Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S
#вставить строку S0
c = input("Введите символ перед которым вставлять S0")
s = input('Введите строку содержащую "с"')
s0 = input('введите что-то')
if s.find(c):
    print(s.replace(c, (s0+c)))
else:
    print("нет символа")