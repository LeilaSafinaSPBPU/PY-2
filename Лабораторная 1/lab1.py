import doctest
# TODO Написать 3 класса с документацией и аннотацией типов


class Professor:
    """
    Класс описывает модель преподаватель.
    """
    def __init__(self, speciality: str, experience: int):
        """ Инициализация экземпляра класса.
        :param speciality: обозначает специализацию преподавателя (предметная область)
        :param experience: обозначает опыт учителя (кол-во оконченных высших образований)
        """
        if experience > 6:
            raise ValueError("Вероятно профессор врет")
        if experience < 1:
            raise ValueError("Профессор не компетентен")
        self.experience = experience
        self.speciality = speciality

    def teaching(self) -> str:
        """
        Метод для обозначения основной деятельности профессора.
        :return возвращает название урока, которое может провести профессор (по своей специализации)
        """
        pass

    def training(self) -> int:
        """
        Метод для обозначения повышения квалификации профессора.
        :return возвращает кол-во часов, проведенных на повышении квалификации
        """
        pass


class Student:
    """
    Класс описывает модель студента.
    """
    def __init__(self, age: int, exam_passed: str):
        """ Инициализация экземпляра класса.
         :param age: возраст студента
         :param exam_passed: сдан или не сдан экзамен студентом
         """
        if age > 30:
            raise ValueError("Недопустимый возраст студента")
        if age < 18:
            raise ValueError("Недопустимый возраст студента")
        self.age = age
        self.exam_passed = exam_passed

    def studying(self):
        """
        Метод для обозначения основной деятельности студента.
        """
        pass

    def exam(self, subject: str, number_exam: int):
        """
        Метод для обозначения конечного этапа обучение
        :param subject: обозначение предмета сдачи экзамена
        :param number_exam: обозначение кол-ва экзаменов
        """
        pass


class Diplom:
    """
    Класс описывает модель диплома.
    """

    def __init__(self, science: str, pages: int):
        """ Инициализация экземпляра класса.
        :param science: предметная область диплома
        :param pages: кол-во страниц диплома
        """
        self.science = science
        self.pages = pages
        if pages > 1000:
            raise ValueError("Недопустимое кол-во страниц для диплома")
        if pages < 20:
            raise ValueError("Недопустимое кол-во страниц для диплома")

    def read(self, current_page: int) -> int:
        """
        Метод для обозначения прочтения диплома.
        :param current_page: текущая страница диплома
        :return: возвращает переменную с типом int
        """
        pass

    def new_page(self):
        """
        Метод для перелистывания страницы.
        """
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod()  # тестирование примеров, которые находятся в документации
