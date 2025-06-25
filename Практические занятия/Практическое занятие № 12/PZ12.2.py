#Составить генератор (yield), который переведет символы строки из верхнего
#регистра в нижний.
def small(slovo):
    for i in slovo:
        yield i.lower()

pish = input("Введите буквы в верхнем регистре: ")

gen = small(pish)
print('Вот буквы в нижнем регистре: ', ''.join(map(str, gen)), end="")