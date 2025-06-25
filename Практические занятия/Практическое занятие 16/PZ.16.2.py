#Создайте класс "Животное", который содержит информацию о виде и возрасте
#животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
#"Животное" и содержат информацию о породе.
class Animal:
    def __init__(self, species, age):
        self.species = species  # вид животного
        self.age = age        # возраст животного

    def get_species(self):
        return self.species

    def get_age(self):
        return self.age


class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)  # вызываем конструктор родительского класса
        self.breed = breed             # порода собаки

    def get_breed(self):
        return self.breed


class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)  # вызываем конструктор родительского класса
        self.breed = breed            # порода кошки

    def get_breed(self):
        return self.breed


# Пример использования
dog = Dog("Собака", 5, "Лабрадор")
print(f"Вид: {dog.get_species()}, Возраст: {dog.get_age()} лет, Порода: {dog.get_breed()}")

cat = Cat("Кошка", 3, "Британская")
print(f"Вид: {cat.get_species()}, Возраст: {cat.get_age()} года, Порода: {cat.get_breed()}")