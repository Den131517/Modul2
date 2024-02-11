class Animal:
    """
    Базовый класс для представления животных.
    """
    def __init__(self, name: str, age: int):
        """
        Конструктор класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает животное.

        :return: Строка с звуком.
        """
        return "Some generic animal sound"

    def __str__(self) -> str:
        """
        Метод для строкового представления объекта.

        :return: Строковое представление объекта.
        """
        return f"{self.name}, {self.age} years old"

    def __repr__(self) -> str:
        """
        Метод для представления объекта в REPL.

        :return: Строковое представление объекта.
        """
        return f"Animal(name={self.name}, age={self.age})"

    def color(self) -> str:
        return "Some random animal color"


class Dog(Animal):
    """
    Класс для представления собак, унаследованный от Animal.
    """
    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def bark(self) -> str:
        """
        Возвращает звук лая собаки.

        :return: Строка с звуком лая.
        """
        return "Woof! Woof!"

    def make_sound(self) -> str:
        """
        Перегруженный метод из базового класса Animal.
        Возвращает звук лая собаки.

        Перегрузка данного метода необходима для
        представления особенности звука собаки.

        :return: Строка с звуком лая.
        """
        return self.bark()

    def __repr__(self) -> str:
        """
        Перегруженный Метод для представления объекта в REPL.
        Добавляет информацию о породе собаки.

        :return: Строковое представление объекта.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"


if __name__ == "__main__":
    animal = Dog('Bob', 13, "alabay")
    print(animal)
    pass
