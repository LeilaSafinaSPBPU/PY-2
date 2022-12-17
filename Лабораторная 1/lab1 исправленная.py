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
        if isinstance(speciality, (str)):
            raise TypeError("Специализация преподавателя должна быть типа str")
        if experience > 6:
            raise ValueError("Вероятно преподаватель врет")
        if experience < 1:
            raise ValueError("Преподаватель не компетентен")
        self.experience = experience
        self.speciality = speciality

    def set_activity_professor(self) -> str:
        """
        Метод для обозначения основной деятельности профессора.
        :return возвращает название урока, которое может провести профессор (по своей специализации)
        """
        pass

    def number_of_groups_(self) -> str:
        """
        Метод для обозначения кол-ва групп, которые ведет профессор
        :return возвращает кол-во групп, которые ведет профессор
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
        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть типа int")
        if age < 18:
            raise ValueError("Недопустимый возраст студента")
        self.age = age


    def set_activity_student(self):
        """
        Метод для обозначения основной деятельности студента.
        """
        pass

    def pass_final_exams(self, subject: str, number_exam: int):
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

    def __init__(self, science: str, pages: int, accepted: str):
        """ Инициализация экземпляра класса.
        :param science: предметная область диплома
        :param pages: кол-во страниц диплома
        :param accepted: принят диплом или нет
        """
        self.science = science
        self.pages = pages
        self.accepted = accepted
        if isinstance(pages, (int, float)):
            raise TypeError("Кол-во страниц должно быть типа int или float")
        if pages > 1000:
            raise ValueError("Недопустимое кол-во страниц для диплома")
        if pages < 20:
            raise ValueError("Недопустимое кол-во страниц для диплома")

    def mistake(self, mistake_page: int, mistake_line: int) -> int:
        """
        Метод для обозначения ошибки на странице диплома.
        :param mistake_page:  страница диплома с ошибкой
        :param mistake_line:  строка диплома с ошибкой
        :return: возвращает переменную с типом int
        """
        pass

    def goto_page(self):
        """
        Метод для перелистывания страницы.
        """
        pass


if __name__ == "__main__":
    Oleg_Petrovic = Professor("Высшая математика", 3)
    Marina_Vasilevna = Professor("Экономика", 2)
    Ivan_Ivanov = Student(21, "Нет")
    Lescha_Okunev = Student(19, "Да")
    diplom_1 = Diplom("Высшая математика", 51, "Да")
    diplom_2 = Diplom("Иностранный язык", 89, "Да")
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass