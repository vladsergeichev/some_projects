class Nikola:
    """
        Задача с сайта - https://smartiqa.ru/python-workbook/class#4
    """

    # Строго задать атрибуты класса
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        if self.name != 'Николай':
            self.name = f'Я не {self.name}, а Николай'
        self.age = age


# Тесты
person1 = Nikola('Николай', 18)
print(person1.name)
person2 = Nikola('Ермек', 25)
print(person2.name)
person2.surname = 'Петров'