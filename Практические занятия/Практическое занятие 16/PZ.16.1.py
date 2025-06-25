#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
#инкремента и декремента значения.

class count:
    def __init__(self, shetintime=0):
        self.val = shetintime  # текущее значение счетчика

    def increment(self, step=1):
        #Увеличивает значение счетчика на заданный шаг (по умолчанию на 1)
        self.val += step

    def decrement(self, step=1):
        #Уменьшает значение счетчика на заданный шаг (по умолчанию на 1)
        self.val -= step

    def func(self):
        #Возвращает текущее значение счетчика
        return self.val

    def reset(self):
        #Сбрасывает счетчик в ноль
        self.val = 0

count = count()  # создаем счетчик с начальным значением 0
print(count.func())  # 0

count.increment()  # увеличиваем на 1
print(count.func())  # 1

count.increment(5)  # увеличиваем на 5
print(count.func())  # 6

count.decrement(2)  # уменьшаем на 2
print(count.func())  # 4

count.reset()  # сбрасываем в ноль
print(count.func())  # 0