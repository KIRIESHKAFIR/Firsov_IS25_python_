#Составить генератор (yield), который переведет символы строки из верхнего
#регистра в нижний.
def small(slovo):
    for i in slovo:
        yield i.lower()
pish = input()
gen = small(pish)
for i in gen:
    print(i, end="")