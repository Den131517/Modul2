import doctest


class Animal:
    def init(self, name, age):
        """
        Создание экземпляра класса Animal

        :param name: Имя животного
        :param age: Возраст животного

        Примеры:
        >>> animal = Animal("Lion", 23 )
        """
        if not isinstance(name, str):
            raise TypeError("Имя животного должно быть строкой")
        if age < 0:
            raise ValueError("Возраст животного должен быть положительным числом")
        self.name = name
        self.age = age

    def get_name(self):
        """
        Возвращает имя животного

        :return: Имя животного

        Примеры:
        >>> animal = Animal("Lion", 23 )
        >>> animal.get_name(self)
        """
        ...

    def get_age(self):
        """
        Возвращает возраст животного

        :return: Возраст животного
        Примеры:
        >>> animal = Animal("Lion", 23 )
        >>> animal.get_name(self)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class Car:
    def init(self, brand, model, year):
        """
        Создание экземпляра класса Car

        :param brand: Марка автомобиля
        :param model: Модель автомобиля

        :param year: Год выпуска автомобиля
        Примеры:
        >>> car = Car("Toyota", "Corolla", 2005)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int):
            raise TypeError("Год выпуска автомобиля должен быть положительным целым числом")
        self.brand = brand
        self.model = model
        self.year = year

    def get_brand(self):
        """
        Возвращает марку автомобиля

        :return: Марка автомобиля

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2005)
        >>> car.get_brand(self)
        """
        ...

    def get_model(self):
        """
        Возвращает модель автомобиля

        :return: Модель автомобиля

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2005)
        >>> car.get_model(self)
        """
        ...

    def get_year(self):
        """
        Возвращает год выпуска автомобиля

        :return: Год выпуска автомобиля

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2005)
        >>> car.get_year(self)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
