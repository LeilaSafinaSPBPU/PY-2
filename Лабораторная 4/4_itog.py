class Museum:
    """ Базовый класс книги. """
    def __init__(self, museum_name: str, location: str):
        """
            Создание и подготовка к работе объекта "Музей"
            :param museum_name: Название музея
            :param location: Местонахождение музея
            Атрибуты museum_name и location изменяться не могут
            Пример:
            >>> museum = Museum('Русский музей', 'Инженерная улица, 2')  #инициализация экземпляра класса
        """

        if not isinstance(museum_name, str):
            raise TypeError("Название музея должно быть типа string")
        self._museum_name = museum_name

        if not isinstance(location, str):
            raise ValueError("Местонахождение музея должно быть типа string")
        self._location = location

    @property
    def museum_name(self):
        return self.museum_name

    @property
    def location(self):
        return self._location

    def __str__(self):
        return f"Название музея {self.museum_name}. Местонахождение {self.location}"

    def __repr__(self):
        return f"{self.__class__.__name__}(museum_name={self.museum_name!r}, location={self.location!r})"

    def existence_of_art(self, current_loc: str) -> bool:
        """
            Функция для определения местонахождения картины в музее
            :param current_loc: Местонахождение картины в музее
            :rise TypeError: Местонахождение должно быть типа str.
            :return: Можно ли увидеть картину
            Пример:
            >>> museum = Museum('Русский музей', 'Инженерная улица')
            >>> museum.existence_of_art('10 зал')
        """
        if not isinstance(current_loc, str):
            raise ValueError("Местонахождение картины должно быть типа string")
        self.current_loc = current_loc
        ...

    def tickets(self, type_of_ticket: str) -> float:
        """
            Функция для расчета количества проданных билетов. Билеты допустим разные: для детей, для студентов , для взрослых и т.д.
            :param type_of_ticket: Тип билета
            :rise TypeError: Тип билета должен быть типа str.
            :return: Количество проданных билетов
            Пример:
            >>> museum = Museum('Русский музей', 'Инженерная улица, 2')
            >>> museum.tickets('Наблюдатель в зале')
        """
        if not isinstance(type_of_ticket, str):
            raise ValueError("Тип билета должен быть типа string")
        self.type_of_ticket = type_of_ticket
        ...


class Department(Museum):
    def __init__(self, museum_name: str, location: str, department_headcount: int):
        """
            Создание и подготовка к работе объекта "Подразделение музея"
            :param department_headcount: численность сотрудников подразделения музея
            Примеры:
            >>> museum_dep = Department('Русский музей', 'Инженерная улица, 2', 126)  #инициализация экземпляра класса
        """
        super().__init__(museum_name, location)

        if not isinstance(department_headcount, int):
            raise TypeError("Количество сотрудников музея должно быть типа int")
        if department_headcount < 0:
            raise ValueError("Количество сотрудников музея не может быть отрицательным числом")
        self.department_headcount = department_headcount

    def __str__(self):
        super().__str__()

    def __repr__(self):
        #перегружаем метод, т.к. появился новый атрибут
        return f"{self.__class__.__name__}(museum_name={self.museum_name!r}, location={self.location!r}, department_headcount={self.department_headcount})"

    def salary(self, position: str) -> float:
        """
            Функция для расчета зарплаты сотрудника
            Перегружаем метод, так как руководство отдела может запросить премии и другие выплаты для определенных сотрудников
            :param position: Должность сотрудника
            :rise TypeError: Должность сотрудника должна быть типа str.
            :return: Зарабатная плата
            Пример:
            >>> museum = Department('Русский музей', 'Инженерная улица, 2')
            >>> museum.position('Наблюдатель в зале')
        """
        if not isinstance(position, str):
            raise ValueError("Должность сотрудника музея должна быть типа string")
        self.position = position
        ...
